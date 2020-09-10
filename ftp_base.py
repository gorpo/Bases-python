
import ftplib


# connect to the FTP server
ftp = ftplib.FTP(host="192.168.0.3", user="gorpo", passwd="")
# force UTF-8 encoding
ftp.encoding = "utf-8"
# the name of file you want to download from the FTP server
file = open('teste.jpg','rb')                  # file to send
ftp.storbinary('STOR kitten.jpg', file)     # send the file
file.close()                                    # close file and FTP
ftp.quit()