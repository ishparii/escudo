# read me

Server log-in:
`ssh data@bigdata.cs.luc.edu`, password: `python4fun`

## to do

1. Build a samples-features matrix. Here, samples will be communication between two IP addresses, where *communication* means that a source IP address sent data to a destination IP address. Thus, every single sample in our dataset will look something like:

```
source_ip | destination_ip | frames | bytes | duration | etc . . .
```
2. Once we've processed all of our data (both passive and ddos), we will combine both to create a larger dataset. Training of our classifier will thus occur on both datasets. Some data should be kept aside purely as a test/verification set. 

