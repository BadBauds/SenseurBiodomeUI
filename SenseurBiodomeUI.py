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
    print event     
    if event["name"]=="click":
      id=event["data"]["id"]
      if id=="button1":
        droid.bluetoothWrite("#ga")
	time.sleep(0.5)
        readAll()
      elif id=="button2":
        valider()
      elif id=="button3":
        droid.bluetoothWrite("#gd")
	time.sleep(0.5)
        btRead()
      elif id=="button4":
        droid.bluetoothWrite("#gr")
	time.sleep(0.5)
        btRead()
      elif id=="button5":
        droid.bluetoothWrite("$sd")
	time.sleep(0.5)
        btRead()
      elif id=="button6":
	toSend = "#tt" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        btRead()
      elif id=="button7":
	toSend = "#td" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        btRead()
      elif id=="button8":
        toSend = "#ru" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        btRead()
      elif id=="button9":
        toSend = "#rd" + droid.fullQueryDetail("editText1").result['text']
        droid.bluetoothWrite(toSend)
	time.sleep(0.5)
        btRead()
      elif id=="button10":
        droid.bluetoothWrite("#as")
	time.sleep(0.5)
        btRead()
      elif id=="togglebutton1":
        if event["data"]["checked"]=="true":
	   droid.bluetoothWrite("#as")
	   print "on"
        else:
           droid.bluetoothWrite("#ds")
	   print "off"
    elif event["name"]=="screen":
      if event["data"]=="destroy":
        return
    elif event["name"]=="key":
      if event["data"]["key"]=='4':
        return


print "Started"
layout="""<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@+id/background" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent" android:background="#ff008080">
    <LinearLayout android:layout_width="match_parent" android:layout_marginBottom="8dip" android:layout_marginLeft="10dip" android:layout_marginTop="15dip" android:id="@+id/linearLayout1">
        <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="Senseur DMX" android:id="@+id/textViewTitre" android:textStyle="bold" android:textSize="10sp" android:textColor="#000" android:gravity="center_vertical|center_horizontal|center"></TextView>
        <ToggleButton android:id="@+id/togglebutton1" android:layout_width="wrap_content" android:layout_height="wrap_content" android:textOn="Senseur" android:textOff="Senseur" android:layout_marginLeft="148dip" android:layout_width="74dip" android:gravity="center_vertical|center_horizontal|center" android:onClick="onToggleClicked"></ToggleButton>
    </LinearLayout>
<View
    android:layout_width="fill_parent"
    android:layout_height="1dp"
    android:background="@android:color/darker_gray"/>
    <LinearLayout android:layout_width="wrap_content" android:layout_marginLeft="10dip" android:layout_marginTop="8dip" android:id="@+id/linearLayout4">
        <LinearLayout android:layout_width="match_parent" android:layout_height="match_parent" android:orientation="vertical" android:id="@+id/linearLayout2">
            <TextView android:layout_width="wrap_content" android:layout_height="46dip" android:text="Distance de la cible: " android:id="@+id/textView1" android:textAppearance="?android:attr/textAppearanceLarge" android:gravity="center_vertical|center_horizontal|center"></TextView>
            <TextView android:layout_width="wrap_content" android:layout_height="46dip" android:text="Delai de passage de la cible : " android:id="@+id/textView2" android:textAppearance="?android:attr/textAppearanceLarge" android:gravity="center_vertical|center_horizontal|center"></TextView>
            <TextView android:layout_width="wrap_content" android:layout_height="46dip" android:text="Duree du sigal DMX : " android:id="@+id/textView3" android:textAppearance="?android:attr/textAppearanceLarge" android:gravity="center_vertical|center_horizontal|center"></TextView>
            <TextView android:layout_width="wrap_content" android:layout_height="46dip" android:text="Marge de detection : " android:id="@+id/textView4" android:textAppearance="?android:attr/textAppearanceLarge" android:gravity="center_vertical|center_horizontal|center"></TextView>
        </LinearLayout>
        <LinearLayout android:layout_width="wrap_content" android:orientation="vertical" android:layout_marginLeft="87dip" android:id="@+id/linearLayout3">
            <EditText android:id="@+id/editText1" android:tag="Tag Me" android:hint="Valeur" android:inputType="textCapWords|textPhonetic|number"></EditText>
            <EditText android:id="@+id/editText2" android:tag="Tag Me" android:hint="Valeur" android:inputType="textCapWords|textPhonetic|number"></EditText>
            <EditText android:id="@+id/editText3" android:tag="Tag Me" android:hint="Valeur" android:inputType="textCapWords|textPhonetic|number"></EditText>
           <EditText android:id="@+id/editText4" android:tag="Tag Me" android:hint="Valeur" android:inputType="textCapWords|textPhonetic|number"></EditText>
        </LinearLayout>
    </LinearLayout>
    <LinearLayout android:layout_width="match_parent" android:layout_marginLeft="245dip" android:layout_marginTop="10dip" android:id="@+id/linearLayout5">
        <Button android:id="@+id/button1" android:layout_width="wrap_content" android:text="Lire"></Button>
        <Button android:id="@+id/button2" android:layout_width="wrap_content" android:text="Valider"></Button>
    </LinearLayout>
    <ImageView android:id="@+id/imageView1" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginLeft="15dip" android:src="file:///sdcard/badbauds.png"></ImageView>
</LinearLayout>
"""


def btRead():
  if droid.bluetoothReadReady().result:
     btRead = droid.bluetoothReadLine().result
     btRead = btRead[btRead.index('#')+1:]
     return btRead

def getBetween(input, limiteGauche, limiteDroite=""):
   if limiteDroite != "":
      toDelete = input[input.index(limiteDroite):]
      input = input.replace(toDelete, "")
   input = input[input.index(limiteGauche):]
   output = input.replace(limiteGauche, "")
   return output

def readAll():
  if droid.bluetoothReadReady().result:
     btRead = droid.bluetoothReadLine().result
     btRead = btRead[btRead.index('#')+1:]
     results = parse(btRead)
     droid.fullSetProperty("editText1","text", results["distance train"])
     droid.fullSetProperty("editText2","text", results["temps train"])
     droid.fullSetProperty("editText3","text", results["temps DMX"])
     droid.fullSetProperty("editText4","text", results["range"])

def parse(input):
   results = {}
   results["distance train"] = getBetween(input, "gt", "gd") + " cm"
   results["distance"] = getBetween(input, "gd", "gr") + " cm"
   results["running time"] = getBetween(input, "gr", "gtt") + " sec"
   results["temps train"] = getBetween(input, "gtt", "gtd") + " sec"
   results["temps DMX"] = getBetween(input, "gtd", "gra") + " sec"
   results["range"] = getBetween(input, "gra", "as") + " cm"
   return results

def valider():
   droid.bluetoothWrite("#st" + droid.fullQueryDetail("editText1").result['text'] + '0')
   time.sleep(0.05)
   droid.bluetoothWrite("#tt" + droid.fullQueryDetail("editText2").result['text'])
   time.sleep(0.05)
   droid.bluetoothWrite("#td" + droid.fullQueryDetail("editText3").result['text'])
   time.sleep(0.05)
   droid.bluetoothWrite("#sr" + droid.fullQueryDetail("editText4").result['text'] + '0')
   time.sleep(0.05)
   btRead()

print layout
print droid.fullShow(layout)
droid.bluetoothWrite("#gs")
time.sleep(0.5)
senseurState = btRead()
print senseurState
if senseurState=='1':
   droid.fullSetProperty("togglebutton1","checked", "true")
elif senseurState=='0':
   droid.fullSetProperty("togglebutton1","checked", "false")
eventloop()
print droid.fullQuery()
print "Data entered =",droid.fullQueryDetail("editText1").result
droid.fullDismiss()
          
