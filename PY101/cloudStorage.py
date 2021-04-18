import dropbox

class TransferData:
    def __init__ (self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox (self.access_token)
        
        f  =open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
    
    def main():
        access_token='sl.AvKySqJ3csaW78bD9I3-jWtaw40V7LnwHhC8Nu5n8NAWqLQRb6C7R304cgUamLVYLlljaEit3W9ghh5q-eDTwluRkykUUNmrhMRPh4cnl1vp77_yd1xINRDHmiA16jgkJhdge44'
        transferData=TransferData(access_token)
        file_from=input("Enter file path that you want to transfer:")
        file_to=input("Enter the file path to upload in dropbox:")
        transferData.upload_file(file_from,file_to)
        print("File has been moved")


