#Lib-Import 
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys 
import ipaddress
import struct
from scapy.layers.inet import IP, UDP
from scapy.layers.dns import DNS, DNSRR, DNSQR, DNSRROPT
from scapy.sendrecv import sr
from scapy.all import get_if_addr, conf
from socket import inet_aton
import logging

#Custom-Modules Importe
import error

#QT-Window ImportP
from UI.mainwindow import Ui_MainWindow

#Logging
# logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w")
# logging.debug("Logging gestartet")

#Window definieren 
class MainWindow(QMainWindow): 
    def __init__(self, parent = None): 
        super().__init__(parent)
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.setWindowTitle("easyDNS v1.7")

        self.ui.btn_send.clicked.connect(self.execute_dns)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_use_ecs.clicked.connect(self.activate_ecs)
        self.ui.btn_use_add.clicked.connect(self.current_address)


        self.ui.lbl_error.hide()
        self.ui.le_ecs_addr.setVisible(False)
        self.ui.lbl_ecs.setVisible(False)

        self.make_item_non_selectable([1, 5, 9])

    def execute_dns(self): 
        query, typ = self.build_dns_query()

        if not query:
            return
        
        ans, unans = sr(query, timeout=5)

        if len(ans) <= 0: 
            self.handle_error("Err14")
            return
        elif ans[0][1][DNS].haslayer("DNS SOA Resource Record"):
            self.ui.lbl_error.setText("Angefragter DNS-Name konnte nicht aufgelöst werden (SOA)")
            self.ui.lbl_error.show()
            return
        else: 
            if typ == 35: 
                self.display_NAPTR(ans)
            elif typ == 33: 
                self.display_SRV(ans)
            elif typ == 1:
                self.display_A_Record(ans)
            else: 
                self.handle_error("Err10")
                return
        
        self.ui.lbl_error.hide()

    def display_NAPTR(self, ans): 
        pkt = ans[0][1]
        i = 0
        responses = []

        if pkt.haslayer(DNSRR): 
            answer_type = ans[0][1][DNS][DNSRR].type
            type_name = self.get_type_value(answer_type)

            while True: 
                try: 
                    answer_value = str(ans[0][1][DNS]["DNS Resource Record"][i].rdata)
                except IndexError:
                    break

                proto, transport = self.check_naptr(answer_value)
                qdomain = self.ui.le_domain.text().strip()
                naptr_data = proto + transport + qdomain
                responses.append(naptr_data)
                i += 1

            
            qtype = self.add_data_head(type_name, type_name, qdomain)
            for i in range(0, len(responses)):
                self.add_data_value(qtype, responses[i])
        else: 
            self.handle_error("Err11")
            return
        
    def display_SRV(self, ans):
        pkt = ans[0][1]
        if pkt.haslayer("DNS SRV Resource Record"): 
            responses = {}
            i = 0
            type_name = "SRV"

            while True: 
                try:
                    proxy = ans[0][1][DNS]["DNS SRV Resource Record"][i].target
                    prio = ans[0][1][DNS]["DNS SRV Resource Record"][i].priority
                    responses.update({str(prio): str(proxy)[2:-1]})
                    i += 1 
                except IndexError: 
                    break   
            
            qtype = self.add_data_head(type_name, type_name, str(ans[0][1][UDP][DNS]["DNS Question Record"].qname)[2:-1])
            for i in range(1, len(responses)+1): 
                value = "Prio: " + str(i) + "0" + " = " + responses[str(i)+"0"]
                self.add_data_value(qtype, value)
            return 
        
        else: 
            self.handle_error("Err12")

    def display_A_Record(self, ans): 
        pkt = ans[0][1]
        if pkt.haslayer(DNSRR): 
            type_name = "A-Record"
            ip = ans[0][1][DNS][DNSRR].rdata
            
            qtype = self.add_data_head(type_name, type_name, str(ans[0][1][DNS][DNSQR].qname)[2:-2])
            self.add_data_value(qtype, ip)
            return 

        else: 
            self.handle_error("Err13")
            return
    
    def add_data_head(self, qtyp, typ, qdomain): 
        qtyp = QTreeWidgetItem(self.ui.tre_result)
        qtyp.setText(0, typ)

        unter_knoten = QTreeWidgetItem(qtyp) 
        unter_knoten.setText(0, "Request")
        unter_knoten.setText(1, str(qdomain))

        return qtyp

    def add_data_value(self, qtyp, data): 
        unter_knoten = QTreeWidgetItem(qtyp) 
        unter_knoten.setText(0, "Answer")
        unter_knoten.setText(1, str(data))

    def build_dns_query(self): 
        domain = self.ui.le_domain.text().strip()
        resolver = self.ui.cob_resolver.currentText()
        typ = self.ui.cob_type.currentText()

        if self.validate_input(domain, resolver, typ):
            typnr = self.get_type_nr(typ)

            if typnr == 1: 
                query = self.get_a_record(domain, resolver)
            elif typnr == 33: 
                query = self.get_srv_record(domain, resolver)
            elif typnr == 35: 
                query = self.get_naptr_record(domain, resolver)
            else: 
                self.handle_error("Err07")
                return 
            
            if self.ui.le_ecs_addr.isVisible(): 
                ecs_rr = self.get_ecs_part()
                query[DNS].rd = 1
                query[DNS].ar = ecs_rr
            else: 
                pass 

            return query, typnr
        else: 
            return 0, 0
        
    def get_ecs_part(self): 
        family = 1  
        prefix_length = 32  
        scope = 0  
        ecs_adress = self.ui.le_ecs_addr.text().strip()

        ecs_data = struct.pack("!HBB4s", family, prefix_length, scope, inet_aton(ecs_adress))
        ecs_option = struct.pack("!HH", 8, len(ecs_data)) + ecs_data

        ecs_rr= DNSRROPT(
            rrname=".",
            type=41,  
            rclass=4096,
            extrcode=0,
            version=0,
            z=0,
            rdlen=len(ecs_option),
            rdata=ecs_option
        )

        return ecs_rr
    
    def get_a_record(self, domain, resolver): 
        query = IP(src=get_if_addr(conf.iface))/UDP()/DNS()
        query[IP].dst = resolver
        query["DNS Question Record"].qname = domain
        query["DNS Question Record"].qtype = 1

        return query
    
    def get_srv_record(self, domain, resolver): 
        query = IP(src=get_if_addr(conf.iface))/UDP()/DNS()
        query[IP].dst = resolver
        query["DNS Question Record"].qname = domain
        query["DNS Question Record"].qtype = 33

        return query

    def get_naptr_record(self, domain, resolver): 
        query = IP(src=get_if_addr(conf.iface))/UDP()/DNS()
        query[IP].dst = resolver 
        query["DNS Question Record"].qname = domain
        query["DNS Question Record"].qtype = 35

        return query

    def ip_validation(self, ip): 
        try: 
            ipaddress.ip_address(ip)
            return False
        except ValueError: 
            return True
        
    def get_type_nr(self, typ):
        if typ == "NAPTR": 
            return 35
        elif typ == "SRV": 
            return 33
        elif typ == "A-Record": 
            return 1
        else: 
            self.handle_error("Err06")
            return
        
    def get_type_value(self, typnr): 
        if int(typnr) == 1: 
            return "A-Record"
        elif int(typnr) == 33: 
            return "SRV"
        elif int(typnr) == 35: 
            return "NAPTR"
        else: 
            self.handle_error("Err08")
            return 
        
    def validate_input(self, domain, resolver, typ): 
        if self.ip_validation(resolver):
            self.handle_error("Err03")
            return False
        
        if type(domain) != str:
            self.handle_error("Err04")
            return False
        if domain == "": 
            self.handle_error("Err04")
            return False

        if type(typ) != str: 
            self.handle_error("Err05")
            return False 
        
        return True

    def check_naptr(self, answer): 
        if (answer.__contains__("sips")): 
            proto = "_sips."
        elif (answer.__contains__("sip")): 
            proto = "_sip."
        else: 
            self.handle_error("Err01")
            return 

        if (answer.__contains__("udp")): 
            transport = "_udp."
        elif (answer.__contains__("tcp")): 
            transport = "_tcp."
        else: 
            self.handle_error("Err02")
            return 

        return proto, transport
    
    def handle_error(self, msg): 
        message = error.error(msg)
        self.ui.lbl_error.setText(message)
        self.ui.lbl_error.show()
    
    def make_item_non_selectable(self, index): 
        for i in index: 
            item = self.ui.cob_resolver.model().item(i)
            item.setEnabled(False)
            font = QFont()
            font.setBold(True)
            item.setFont(font)

    def reset(self): 
        self.ui.le_domain.setText("")
        self.ui.cob_type.setCurrentText("NAPTR")
        self.ui.lbl_error.hide()
        self.ui.lbl_error.setText("")
        self.ui.tre_result.clear()
        self.ui.le_ecs_addr.setText("")
        self.ui.cob_resolver.setCurrentIndex(0)

    def activate_ecs(self): 
        self.ui.le_ecs_addr.setVisible(not self.ui.le_ecs_addr.isVisible())
        self.ui.lbl_ecs.setVisible(not self.ui.lbl_ecs.isVisible())

        if self.ui.le_ecs_addr.isVisible(): 
            self.ui.btn_use_ecs.setText("Disable ECS")
        else: 
            self.ui.btn_use_ecs.setText("Enable ECS")

    def current_address(self):
        selectedItems = self.ui.tre_result.selectedItems()
        if selectedItems: 
            selectedItem = selectedItems[0]
            addr = selectedItem.text(1)
            
            self.ui.le_domain.setText(addr)

    def exit(self): 
        window.close()

#Window aufbauen
app = QApplication(sys.argv)
window = MainWindow() 
window.show() 

sys.exit(app.exec())
