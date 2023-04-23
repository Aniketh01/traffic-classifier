## Traffic classifier

**Step 1:** Process pcap to produce intermediary nDPI results: `sh  parse_via_ndpi.sh`

The script **parse_via_ndpi.sh** is the reference point for this. It takes an input directory with pcaps. This script specifically expects the following structure:

```
|<Input directory>
|-- xiaomi-induction
|   |-- 2022-12-23_15.18.39_192.168.10.222.pcap
|   |-- 2022-12-24_15.18.40_192.168.10.222.pcap
|   |-- 2022-12-25_15.18.40_192.168.10.222.pcap
|   |-- 2022-12-26_15.18.40_192.168.10.222.pcap
|   |-- 2022-12-27_15.18.41_192.168.10.222.pcap
|   `-- 2022-12-28_15.18.41_192.168.10.222.pcap
|-- xiaomi-ricecooker
|   |-- 2022-12-23_18.12.12_192.168.10.197.pcap
|   |-- 2022-12-24_18.12.12_192.168.10.197.pcap
|   |-- 2022-12-25_18.12.18_192.168.10.197.pcap
|   |-- 2022-12-26_18.12.19_192.168.10.197.pcap
|   |-- 2022-12-27_18.12.33_192.168.10.197.pcap
|   `-- 2022-12-28_18.12.56_192.168.10.197.pcap
```

Then, produces a final directory with the CSV and JSON files with traffic flows classified by nDPI. You will need to set the `source_dir="" and final_dir=""` in the bash script. 

**Step 2:** Read the intermediate results produces and process them: `python3 process_ndpi_result.py`

Use this script as reference and based on the structure of your pcap. This script was developed to process the pcaps shared with NEU from their lab. Essentially, the pcap only contained local device communication and therefore, I didn't have to do any filtering at the nDPI level. If you prefer to do that at the nDPI level, you can adjust the script to do so. Finally, the script also corrects few flows with where labelled incorrectly based on our analysis comparing tshark results. 





hich are labelled incorrectly. 
