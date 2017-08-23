import os
import re
import time


from uiautomator import Device

class UC:
    def DownloadUCBrowserFromPlayStore(self,d):
        print('Downloading')													# Created object d for device class
        playstore = d(className='android.widget.TextView', text='Play Store')    # Created object for play store
        playstoreSearch = d(resourceId='com.android.vending:id/search_box_idle_text')   # Created object for play store search
        Searchquery = d(resourceId='com.android.vending:id/search_box_text_input', text='Search Google Play') 
        time.sleep(4)
        Install = d(className='android.widget.Button', text='INSTALL')
        Accept = d(resourceId='com.android.vending:id/continue_button', text='ACCEPT')
        Unistall= d(className='android.widget.Button', text='UNINSTALL')

        if not d.screen.on():            # Check for the screen 
            d.wakeup()						# If off awake the screen

        d.freeze_rotation()						# Freeze the current rotation 

        d.press.home()							 
        time.sleep(5)
        flag =0
        for i in range(10):
            time.sleep(5)
            d.swipe(624,452,100,426)            # Hardcoded the co-ordinates for changing the page.                                

            if playstore.exists:				# Check for the play store on the current screen 
                playstore.click()
                time.sleep(5)
                flag=1
                break
        if flag==1:
                playstoreSearch.click()       # Search bar 
                time.sleep(5)
                Searchquery.set_text('UC Browser')		# Search for UC Browser  
                time.sleep(5)
                d.press.enter()
                time.sleep(5)

                if Install.exists:
                    Install.click()
                    time.sleep(5)
                    Accept.click()         # Accepting T&C



        if Ucobj.WaitForObject(Unistall):        # Here waiting for the button with the uninstall text on it to make sure that UC is not preinstalled 
            print('success full download')
        else:
        	print('Failed to download UC Browser')

    def WaitForObject(self,obj):   # This will wait untill uninstall object appears and break once object found
        count =0
        global brk
        brk=0
        while True:
            time.sleep(5)
            if obj.exists:
                brk=1
                return True

            count +=1
            if count==200:           # Loop will continue till 200 iterations 
                brk=1
                return False
            if brk==1:
                break
    def OpenUCAndDownloadSong(self,d):		# For songs download
        print('opening UC')
        time.sleep(5)
        URL='https://songpk.mobi/categorysimple.php?id=17335'      # Hard coded URL
        open1= d(className='android.widget.Button', text='OPEN')
        EnterUC= d(className='android.widget.TextView', text='Enter UC')
        SearchUC= d(className='android.widget.TextView', text='Search or Enter URL')
        SearchURl= d(className='android.widget.EditText', text='Search or Enter URL')
        DwnloadPage=d(className='android.widget.FrameLayout', packageName='com.UCMobile.intl')
        DwnloadSong= d(className='android.widget.TextView', text='Download')
        NothnksPopup= d(className='android.widget.Button', text='No, thanks.')

        open1.click()
        time.sleep(5)
        check =Ucobj.WaitForObject(EnterUC)
        check =True
        if check:
            
           	EnterUC.click()
            time.sleep(5)
            if NothnksPopup.exists:
            	NothnksPopup.click()
            time.sleep(5)
            SearchUC.click()
            time.sleep(5)
            SearchURl.set_text(URL)      # Passing the URL
            time.sleep(5)
            d.press.enter()
            time.sleep(15)
            print('page is displayed')
            time.sleep(5)
            
            for i in range(9):
                time.sleep(2)
                print("Song Count-->"+str(i))
                if i > 0 :
                    print('swipe')
                    d.swipe(108,974,128,753)   # Params (start X, start Y, end X, end Y)
                    time.sleep(5)
                d.click(128,753)
                time.sleep(10)
                d.click(337,407)
                time.sleep(5)
                if DwnloadSong.exists:
                    DwnloadSong.click()
                    time.sleep(3)
                    DwnloadSong.click()
                    time.sleep(3)
                    d.press.back()
                    time.sleep(3)



    def GetListOfSongsFromPhone(self):
        time.sleep(1800) 													# half and hour for download
        command = 'adb -s f9a159df shell ls /sdcard/UCDownloads/*.mp3'      # List out the all the .mp3 format
        f =os.popen(command).read()
        count =re.findall('.mp3',f)								# Listing all the .mp4 format files 
        print(len(count))
        if count == 10:
            print('successfull download')



if __name__=="__main__":
    Ucobj =UC()
    d = Device('f9a159df')    # Device serial key


   	Ucobj.DownloadUCBrowserFromPlayStore(d)
    Ucobj.OpenUCAndDownloadSong(d)
    Ucobj.GetListOfSongsFromPhone()
    print('done')