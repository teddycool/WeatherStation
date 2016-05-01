package com.sundback.psk.wstation1;


import android.util.Log;

public final class ShLog {

    public static void Print(char level, java.lang.String tag, java.lang.String message)         {
        if(level=='d'){
           Log.d("WSTATION " + tag, message);
        }
        if(level=='i'){
            Log.i("WSTATION " + tag, message);
        }

    }

}
