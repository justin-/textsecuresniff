package com.poc.dumplog;

import android.os.Bundle;
import android.app.Activity;
import android.util.Log;
import android.view.Menu;
import android.os.Environment;
import java.io.*;

public class MainActivity extends Activity {

	private static final String TAG = "MainActivity";
	
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        dump();
        setContentView(R.layout.activity_main);
    }

private void dump()
{	
    try
    {   
        File path = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS);
        File file = new File(path, "logcat");
        
        if (file.exists())
        	file.delete();
        
        OutputStream os = new FileOutputStream(file);
        
        Process process = Runtime.getRuntime().exec("logcat -d");
        BufferedReader buffer = new BufferedReader(new InputStreamReader(process.getInputStream()));
                         
        StringBuilder log = new StringBuilder();
        String line;
        while ((line = buffer.readLine()) != null)
        {
        	log.append(line + System.getProperty("line.separator"));
        }
        
    	os.write(log.toString().getBytes("UTF-8"));
        os.close();
          
    }
    catch (Exception ex)
    {
        Log.e(TAG, ex.getLocalizedMessage());
    }
}
        
}
