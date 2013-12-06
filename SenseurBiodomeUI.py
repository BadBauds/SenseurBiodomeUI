import android
import time
from threading import Thread

droid=android.Android()

uuid='00001101-0000-1000-8000-00805F9B34FB' #couldn't get bluetooth to work without this uuid..
mac='20:13:08:13:00:26' #bluetooth module mac address

droid.toggleBluetoothState(True) #turn on bluetooth
connId=droid.bluetoothConnect(uuid,mac).result #connect to bluetooth moduel mac specified above
time.sleep(2)


def eventloop():
  while True:
    event = droid.eventWait().result      
    if event["name"]=="click":
      id=event["data"]["id"]
      if id=="button1":
	toSend = "#st" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        readSerial()
      elif id=="button2":
        droid.bluetoothWrite("#gt")
	time.sleep(0.5)
        readSerial()
      elif id=="button3":
        droid.bluetoothWrite("#gd")
	time.sleep(0.5)
        readSerial()
      elif id=="button4":
        droid.bluetoothWrite("#gr")
	time.sleep(0.5)
        readSerial()
      elif id=="button5":
        droid.bluetoothWrite("$sd")
	time.sleep(0.5)
        readSerial()
      elif id=="button6":
	toSend = "#tt" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        readSerial()
      elif id=="button7":
	toSend = "#td" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        readSerial()
      elif id=="button8":
        toSend = "#ru" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        readSerial()
      elif id=="button9":
        toSend = "#rd" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        readSerial()
      elif id=="button10":
        droid.bluetoothWrite("#as")
	time.sleep(0.5)
        readSerial()
    elif event["name"]=="screen":
      if event["data"]=="destroy":
        return
    elif event["name"]=="key":
      if event["data"]["key"]=='4':
        return


print "Started"
layout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
        android:id="@+id/background"
        android:orientation="vertical" android:layout_width="match_parent"
        android:layout_height="match_parent" android:background="#ff008080">
        <LinearLayout android:layout_width="match_parent"
                 android:id="@+id/linearLayout1">
        <EditText android:layout_width="match_parent"
                 android:layout_width="240dp" android:id="@+id/editText1"
                android:tag="Tag Me" android:hint="Valeur" android:inputType="textCapWords|textPhonetic|number">
                <requestFocus></requestFocus>
        </EditText>
                <Button android:id="@+id/button1"  android:layout_width="120dp" android:layout_height="70dp"
                         android:text="Ajuster distance train"></Button>
        </LinearLayout>
        <LinearLayout android:layout_width="match_parent"
                 android:id="@+id/linearLayout1">
                <Button android:id="@+id/button2" android:layout_width="120dp" android:layout_height="70dp"
                         android:text="Voir distance train"></Button>
                <Button android:id="@+id/button3"  android:layout_width="120dp" android:layout_height="70dp"
                         android:text="Voir distance percu"></Button>
                <Button android:id="@+id/button4" android:layout_width="120dp" android:layout_height="70dp"
                         android:text="Voir temps de marche"></Button>
        </LinearLayout>
     <LinearLayout android:layout_width="match_parent"
                 android:id="@+id/linearLayout1">
                <Button android:id="@+id/button5" android:layout_width="120dp" android:layout_height="70dp"
                         android:text="Partir DMX"></Button>
                <Button android:id="@+id/button6"  android:layout_width="120dp" android:layout_height="70dp" android:layout_gravity="center"
                         android:text="Ajuster temps train"></Button>
                <Button android:id="@+id/button7" android:layout_width="120dp" android:layout_height="70dp" android:layout_gravity="center"
                         android:text="Ajuster temps DMX"></Button>
        </LinearLayout>
     <LinearLayout android:layout_width="match_parent"
                 android:id="@+id/linearLayout1">
                <Button android:id="@+id/button8" android:layout_width="120dp" android:layout_height="70dp"
                         android:text="Ajuster valeur superieure"></Button>
                <Button android:id="@+id/button9"  android:layout_width="120dp" android:layout_height="70dp"
                         android:text="Ajuster valeur inferieur"></Button>
                <Button android:id="@+id/button10" android:layout_width="120dp" android:layout_height="70dp" android:layout_gravity="center"
                         android:text="Activer/Desactiver senseur"></Button>
        </LinearLayout>
        <LinearLayout>
        <EditText android:layout_width="match_parent"
                 android:layout_width="120dp" android:hint="Resultat" android:id="@+id/editText2"
                android:tag="Tag Me">
                <requestFocus></requestFocus>
        </EditText>
        <ImageView
                android:id="@+id/imageView1"
                android:layout_width="wrap_content"
                android:layout_height="wrap_content"
                android:layout_marginLeft="15dp"
                android:src="file:///sdcard/badbauds.png">
        </ImageView>
</LinearLayout>
</LinearLayout>
"""


def readSerial():
  btRead = droid.bluetoothRead().result
  print btRead
  if btRead == 'error':
    droid.makeToast("Senseur hors de portee")
  else:
    droid.fullSetProperty("editText2","text", btRead)

print layout
print droid.fullShow(layout)
eventloop()
print droid.fullQuery()
print "Data entered =",droid.fullQueryDetail("editText1").result
droid.fullDismiss()
          
