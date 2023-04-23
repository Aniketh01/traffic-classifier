ndpi_res = ''

df_list = []

# Specify the columns you want to keep
# columns_to_keep = ['#flow_id', 'protocol', 'first_seen', 'last_seen', 'duration', 'src_ip', 'src_port', 'dst_ip', 'dst_port', 'ndpi_proto_num', 'ndpi_proto', 'proto_by_ip', 'server_name_sni',
#                   'server_info', 'tls_version', 'ja3c', 'tls_client_unsafe', 'ja3s', 'tls_server_unsafe', 'advertised_alpns', 'negotiated_alpn', 'tls_supported_versions', 'ssh_client_hassh', 'ssh_server_hassh', 'flow_info', 'plen_bins',
#                   'http_user_agent']

columns_to_keep = ['#flow_id', 'protocol', 'first_seen', 'last_seen', 'duration', 'src_ip', 'src_port', 'dst_ip', 'dst_port', 'ndpi_proto_num', 'ndpi_proto', 'server_name_sni',
                  'server_info', 'tls_version', 'ja3c', 'tls_client_unsafe', 'ja3s', 'tls_server_unsafe', 'advertised_alpns', 'negotiated_alpn', 'tls_supported_versions', 'ssh_client_hassh', 'ssh_server_hassh', 'flow_info', 'plen_bins',
                  'http_user_agent']

for csv_file in glob.glob(os.path.join(ndpi_res, "*.csv")):
    split_path = re.split(r'(-\d{4}-\d{2}-\d{2})', csv_file)
    #NOTE: This script was specifically written to process NEU lab results. Probably need to adapt this for your needs.
    device_name = split_path[0].replace('/home/aniketh/devel/src/IoT-local/parsed_dec_new_with_guessing/', '')
    with open(csv_file, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']

    df = pd.read_csv(csv_file, usecols=columns_to_keep, index_col=False)

    df['device_name'] = device_name
    df['file_path'] = csv_file

    df_list.append(df)

# Concatenate all DataFrames into a single DataFrame
df_ndpi = pd.concat(df_list, ignore_index=True)
df_ndpi.loc[(df_ndpi['ndpi_proto'] == 'CiscoVPN') & (df_ndpi['dst_port'] == 8008), 'ndpi_proto'] = 'SSDP'
df_ndpi = df_ndpi[df_ndpi['ndpi_proto'] != 'BitTorrent']
df_ndpi = df_ndpi[df_ndpi['ndpi_proto'] != 'EthernetIP']
df_ndpi.to_csv("ndpi_results.csv")
