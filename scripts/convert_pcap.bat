@echo off

set PCAP_FILE_NAME=%1
set OUTPUT_FILE_NAME=%2
set COMMAND=tshark -r %PCAP_FILE_NAME% -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e ip.proto -e frame.len -e _ws.col.Info -E header=y -E separator=, -E quote=d -E occurrence=f 

start /min cmd /c %COMMAND% ^> %OUTPUT_FILE_NAME%
