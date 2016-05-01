package com.sundback.psk.wstation1;

import android.annotation.SuppressLint;
import android.app.Dialog;
import android.app.ProgressDialog;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.os.Handler;
import android.view.MotionEvent;
import android.view.View;
import android.widget.TextView;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;

import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;

/**
 * An example full-screen activity that shows and hides the system UI (i.e.
 * status bar and navigation/system bar) with user interaction.
 */
public class Temperatures extends AppCompatActivity {

    static final int PROGRESS_DIALOG = 0;
    private ProgressDialog progressDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_temperatures);
     }


    @Override
    protected void onPostCreate(Bundle savedInstanceState) {
        super.onPostCreate(savedInstanceState);
    }

    @Override
    public void onStart() {
        super.onStart();
        //TODO: set up timer for receiving values from server
        //TODO: update in separate thread
        String urls = "";
        URL url = null;
        GetCurrentValuesFromServer asyncGetValues = new GetCurrentValuesFromServer();
        urls =  "http://www.sundback.com/ws/getcurrentdata.php";
        ShLog.Print('d', "URL: " + urls, "ALL");

        try {
            url = new URL(urls);
        } catch (MalformedURLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        catch (Exception e)                               {
            e.printStackTrace();
        }
        ShLog.Print('d', "SENT URL:", url.toString());
        asyncGetValues.execute(url);

     }

    @Override
    public void onStop() {
        super.onStop();


    }

    @Override
    protected Dialog onCreateDialog(int id) {
        //dba = new DbAdapter(ShopperMenu.this);
        progressDialog = new ProgressDialog(Temperatures.this);
        progressDialog.setProgressStyle(ProgressDialog.STYLE_SPINNER);
        progressDialog.setMessage("Hämtar värden från servern...");
        progressDialog.setCancelable(true);
        return progressDialog;
    }


    private class GetCurrentValuesFromServer extends AsyncTask<URL, String, Integer> {

        @Override
        protected Integer doInBackground(URL... params) {

            // Get the XML
            URL url;
            try {
                url = params[0];
                ShLog.Print('d',"USED URL:", url.toString());

                URLConnection connection;
                connection = url.openConnection();

                HttpURLConnection httpConnection = (HttpURLConnection)connection;
                //String msg = httpConnection.getResponseMessage();
                // String error = httpConnection.getErrorStream().toString();
                int responseCode = httpConnection.getResponseCode();
                ShLog.Print('d',"HTTP ResponseCode: ", String.valueOf(responseCode));
                if (responseCode == HttpURLConnection.HTTP_OK) {
                    InputStream in = httpConnection.getInputStream();

                    DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
                    DocumentBuilder db = dbf.newDocumentBuilder();

                    // Parse the item feed.
                    Document dom = db.parse(in);
                    Element docEle = dom.getDocumentElement();
                    NodeList nl = docEle.getElementsByTagName("measure");
                    ShLog.Print('d',"refreshItems","No of nodes in xml: " + String.valueOf(nl.getLength()));
                    //NodeList nl = nle.item(0).getChildNodes();
                    if (nl != null && nl.getLength () == 1) {
                            Element measurenode = (Element)nl.item(0);
                            Measure measure = new Measure(measurenode);
                        TextView t = (TextView)findViewById(R.id.outdoorlable);
                        t.setText(measure.getOutdoortemp() + " " + measure.getOutdoorhum());

                                ShLog.Print('d', "Measure: ", measure.toString());
                    }
                }
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (ParserConfigurationException e) {
                e.printStackTrace();
            } catch (SAXException e) {
                e.printStackTrace();
            }
            finally {
            }

            return null;
        }

        @Override
        protected void onPreExecute(){
            showDialog(PROGRESS_DIALOG);
            ShLog.Print('d',"onPreExecute", "showDialog(PROGRESS_DIALOG)");
        }

        @Override
        protected void onPostExecute(Integer result) {
            progressDialog.hide();
            progressDialog.dismiss();
            dismissDialog(PROGRESS_DIALOG);
            ShLog.Print('d',"onPostExecute", "dissmissDialog(PROGRESS_DIALOG)");
        }

    }
}
