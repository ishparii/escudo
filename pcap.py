__author__ = 'Leonid'
from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip
import binascii

testcap = open('test.pcap', mode='rb')
capfile = savefile.load_savefile(testcap, layers=0, verbose=True)
print(capfile)

header = capfile.header
print(header)

packets = capfile.packets
pkt1 = packets[1000]
print(pkt1.timestamp)

eth_frame = ethernet.Ethernet(pkt1.raw())
print(eth_frame)
