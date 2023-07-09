import speedtest 
st = speedtest.speedtest()
download = st.download() / 10**6
upload = st.upload() / 10**6

print("Download: " , download, "mb")
print("Upload: " , upload, "mb")