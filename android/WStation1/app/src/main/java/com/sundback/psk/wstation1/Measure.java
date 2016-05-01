package com.sundback.psk.wstation1;


import org.w3c.dom.Element;
import org.w3c.dom.Node;

/**
 * Created by IntelliJ IDEA.
 * User: psk
 * Date: 2012-03-15
 * Time: 21:04
 * To change this template use File | Settings | File Templates.
 */
public class Measure {
    private String fridgetemplow;
    private String fridgetemphigh;
    private String freezertemp;
    private String outdoortemp;
    private String outdoorhum;
    private String outdoorbar;
    private String indoortemp;
    private String indoorhum;




    //Getters
    public String getFridgetemplow() { return fridgetemplow;    }
    public String getFridgetemphigh() { return fridgetemphigh; }
    public String getFreezertemp() { return freezertemp;   }
    public String getOutdoortemp() {  return outdoortemp; }
    public String getOutdoorhum() {  return outdoorhum;  }
    public String getOutdoorbar() { return outdoorbar;  }
    public String getIndoortemp() { return indoortemp;    }
    public String getIndoorhum() {  return indoorhum;  }


    //Constructor with argument as xml for use when measure added from web
    public Measure(Element measure) {
        //Extract elements
        Element elementfridgetemplow = (Element) measure.getElementsByTagName("fridgetemplow").item(0);
        Element elementfridgetemphigh = (Element) measure.getElementsByTagName("fridgetemphigh").item(0);
        Element elementfreezertemp = (Element) measure.getElementsByTagName("freezertemp").item(0);
        Element elementoutdoortemp = (Element) measure.getElementsByTagName("outdoortemp").item(0);
        Element elementoutdoorhum = (Element) measure.getElementsByTagName("outdoorhum").item(0);
        Element elementoutdoorbar = (Element) measure.getElementsByTagName("outdoorbar").item(0);
        Element elementindoortemp = (Element) measure.getElementsByTagName("indoortemp").item(0);
        Element elementindoorhum = (Element) measure.getElementsByTagName("indoorhum").item(0);


        //Create correct datatypes from elements
        if (elementfridgetemplow.getFirstChild() != null)
            this.fridgetemplow = elementfridgetemplow.getFirstChild().getNodeValue();
        if (elementfridgetemphigh.getFirstChild() != null)
            this.fridgetemphigh = elementfridgetemphigh.getFirstChild().getNodeValue();
        if (elementfreezertemp.getFirstChild() != null)
            this.freezertemp = elementfreezertemp.getFirstChild().getNodeValue();


    }
    @Override
    public String toString() {
        return this.fridgetemphigh + ": "  ; //  + ", " + this.inBasket;
    }


}