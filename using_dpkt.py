# A demonstration of how to use dpkt to inspect packets. This particular
# pcap file contains the TCP/HTTP of a file transfer. For a more detailed
# explanation of the process, see Jon Oberheide's tutorial at:
# https://jon.oberheide.org/blog/2008/10/15/dpkt-tutorial-2-parsing-a-pcap-file/

# python 2 library, doesn't work in python 3
import dpkt

f = open('tcp-http.pcap')
pcap = dpkt.pcap.Reader(f)

for ts, buf in pcap:        # For timestamp, packet in the pcap file
    eth = dpkt.ethernet.Ethernet(buf) # Extract into ethernet object
    ip = eth.data                     # packet.data is the IP object
    tcp = ip.data                     # packet.data.data is the TCP object

    # If the destination port is 80 (indicating an HTTP request) and there
    # exists data beyond the TCP layer available for parsing:
    if tcp.dport == 80 and len(tcp.data) > 0:
        http = dpkt.http.Request(tcp.data)
        print(http.uri)
        print(http.version)
        print(http.method)
        print(http.headers['user-agent'])

f.close()
