#test_app.py
#upload and download speed





def test_get_ip():
    ip_info = getIP()
    assert "IPv6 Address" in ip_info
    assert "Location" in ip_info
    assert "Download Speed" in ip_info
    assert "Upload Speed" in ip_info
    

