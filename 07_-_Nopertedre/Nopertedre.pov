#include "colors.inc"

camera {
    location < 2, 1.5, 1 >
    look_at  < 0, 0, 0>
    right    <4/3,  0,  0>
}

light_source { <10, 10, 05> color White }

#declare   blue1 = pigment { color rgb < 48/255, 130/255, 160/255> }
#declare    red1 = pigment { color rgb <150/255,  60/255,  70/255> }
#declare yellow1 = pigment { color rgb <255/255, 177/255,  65/255> }
#declare  green1 = pigment { color rgb < 10/255, 110/255,  80/255> }

#declare C1 = < 152024884,  210152163,          0> /   259375205;
#declare C2 = <6632738028, 3980949609, 6106948881> / 10000000000;
#declare C3 = <8193990033, 1230614493, 5298215096> / 10000000000;

#declare  V = array[90];

#for (i, 0, 14)
    #for (j, 0, 1)
        #declare V[i+15*j+00] = (1-2*j) * <C1.x*cos(2*pi*i/15) + C1.z*sin(2*pi*i/15), C1.y, -C1.x*sin(2*pi*i/15) + C1.z*cos(2*pi*i/15)>;
        #declare V[i+15*j+30] = (1-2*j) * <C2.x*cos(2*pi*i/15) + C2.z*sin(2*pi*i/15), C2.y, -C2.x*sin(2*pi*i/15) + C2.z*cos(2*pi*i/15)>;
        #declare V[i+15*j+60] = (1-2*j) * <C3.x*cos(2*pi*i/15) + C3.z*sin(2*pi*i/15), C3.y, -C3.x*sin(2*pi*i/15) + C3.z*cos(2*pi*i/15)>;
    #end
#end

#for (i, 0, 89)
    sphere { V[i], 0.02 texture { blue1 } }
#end

#for (i, 0, 88)
    #for (j, i+1, 89)
        #if (vlength(V[i] - V[j]) < 0.45)
            cylinder { V[i], V[j], 0.01 texture {blue1} }
        #end
        #if ( (i < 30) & (j>29) )
            #if (vlength(V[i] - V[j]) < 0.60)
                cylinder { V[i], V[j], 0.01 texture {blue1} }
            #end
        #end
    #end
#end
