load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/shea_util.ncl"

begin
a = asciiread("MeanOND.txt",(/27/),"float")
f = addfile("ersst.mnmean.v5.nc","r")
;indata2= addfile("F:/data/hgt.mon.mean.nc","r")
hgt1=f->sst(:,:,:)
;printVarSummary(hgt1)

time=ispan(1979,2005,1)
time@units="years since 1979 00:00:0.0"    
a!0="time"
a&time=time

t=f->sst (0:323,:,:); 1979-2005-12*27-1=323; 0=1979; 323=2005

wt1 = new((/27,73,144/),"float")
wt1!0 = "time"
wt1!1 = "lat"
wt1&lat = hgt1&lat
wt1!2 = "lon"
wt1&lon = hgt1&lon
wt1@_FillValue = -1e+30
do i=0,26
wt1(i,:,:) = dim_avg_n_Wrap(t(((i*12)+9):((i*12)+10),:,:),0)
end do
printVarSummary(wt1)


WT1=wt1(lat|:,lon|:,time|:)


rc1   = escorc(a,WT1)  
rc1!0 = "lat"
rc1&lat = hgt1&lat
rc1!1 = "lon"
rc1&lon = hgt1&lon
rc1@_FillValue =  -9.99e+08
printVarSummary(rc1)           ; variable overview

 siglev= 0.95            ; a-priori specified sig level
 prob1  = 1.- rtest(rc1, 54, 0)
 prob1@_FillValue =rc1@_FillValue
 prob1 = where( (prob1.le.siglev).or.(prob1.eq.1), \
                           prob1@_FillValue, prob1 )
 copy_VarMeta(rc1,prob1) 




wks = gsn_open_wks("pdf","cor_RFsst")   
gsn_define_colormap(wks,"BlueWhiteOrangeRed")
plot = new(1,graphic) 



  latN   =  20. 
  latS   =  -20.
  lonL   = 20.
  lonR   =  80.  
  
  
  
  
res =True
res@mpFillOn             = True     ; turn off map fill
res@mpMinLatF            = latS         ; zoom in on map
res@mpMaxLatF            = latN

res@gsnDraw              = False          
res@gsnFrame             = False  
res@gsnAddCyclic         = True     
res@mpCenterLonF         = 90.
res@gsnPolar   = "NH" 
res@gsnLeftStringFontHeightF=30
 res@cnHighLabelsOn       = True
res@cnHighLabelBackgroundColor  =-1
res@cnLowLabelsOn        =True
res@cnLowLabelBackgroundColor   =-1
res@mpFillOn             = True         
res@cnLinesOn            = False      
res@cnLineLabelsOn       = False      
res@lbLabelBarOn         = False
res@cnFillOn             = True   
res@cnLevelSelectionMode = "ExplicitLevels"    			; set explicit contour levels
res@cnLevels    = (/-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.30,-0.25,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6/)
res@cnFillColors  =  (/2,6,9,13,20,27,38,54,68,81,96,99,108,144,149,158,173,186,200,216,225,232,239,243,250,255/)


res@gsnContourZeroLineThicknessF = 0 	    ; eliminates zero contour
res@gsnContourNegLineDashPattern = 1       ; sets negative contours to dash pattern 1
 res2                        = True 
   res2@cnLinesOn           = False
  res2@cnInfoLabelOn        = False
  res2@cnLineLabelsOn       = False

  res2@cnFillOn             = True
  res2@cnMonoFillColor      = True
  res2@cnFillColor          = "gray15"
  res2@cnFillPattern        = 17
  res2@cnFillScaleF         = 0.35
  res2@cnFillDotSizeF       = 0.0001
res@gsnLeftString  =  ""
plot(0)=gsn_csm_contour_map_overlay(wks,rc1(:,:),prob1,res,res2)


pres=True
pres@gsnPanelLabelBar=True
pres@lbLabelStride  =2
pres@txString    ="ObservedRF_cor_ERSST"
res@cnLevels    = (/-0.6,-0.55,-0.5,-0.45,-0.4,-0.35,-0.30,-0.25,-0.2,-0.15,-0.1,-0.05,0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6/)
res@cnFillColors  =  (/2,6,9,13,20,27,38,54,68,81,96,99,108,144,149,158,173,186,200,216,225,232,239,243,250,255/)


gsn_panel(wks,plot,(/1,1/),pres)

end
