@echo off
for /r %%i in (*.pcap) do (
	call convert_pcap.bat %%i %%i.csv
)