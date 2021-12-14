;*************************************************
; corel_3.ncl
;
; Concepts illustrated:
;   - Calculating a two-dimensional correlation in time
;   - Reordering an array
;   - Copying attributes from one variable to another
;   - Copying coordinate arrays from one variable to another
;
;************************************************
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_code.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/gsn_csm.ncl"
load "$NCARG_ROOT/lib/ncarg/nclscripts/csm/contributed.ncl"
begin
;***********************************************
  ;Study period
  ;yrStrt     = 1979
  ;yrLast     = 2005
;************************************************
; open file and read in variable
;***********************************************
  in1  = addfile("ens_sst1.nc","r")
  in2  = addfile("HadISST1.nc","r")
  
  tmp1 = in1->sst
  tmp2 = in2->sst
;************************************************
; reorder to get time as right most dimension
;***********************************************
  ts1 = tmp1(lat|:,lon|:,time|:)
  ts2 = tmp2(latitude|:,longitude|:,time|:)
  ;Define new arrray 
  new = ts1(::-1,:,:) 
printVarSummary(tmp1)
printVarSummary(tmp2)
;************************************************
; calculate cross correlations
  maxlag = 2                                    ; set lag
; note, the max lag should not be more than N/4
  
  ccr = esccr(ts1,ts2, maxlag)                   ; calc cross correlations

; copy meta data and coordinate variables using contributed functions
  copy_VarAtts(ts1, ccr)                    
  copy_VarCoords_1(ts2,ccr)
;************************************************
; plot the correlations
;************************************************
  wks  = gsn_open_wks("pdf","corel")              ; open a ps plot
  gsn_define_colormap(wks,"BlWhRe")              ; choose colormap
 
  res                      = True                ; make plot mods

  res@cnFillOn             = True                ; turn on color

;---These two resources not needed in NCL V6.1.0
  res@gsnSpreadColors      = True                ; use full colormap

;---This resource defaults to True in NCL V6.1.0
  res@lbLabelAutoStride    = True                ; automatic lb label stride

  res@cnLinesOn            = False               ; turn off contour lines
  res@cnLevelSelectionMode = "ManualLevels"      ; manually set cn levels
  res@cnMinLevelValF       = -1.                 ; min level
  res@cnMaxLevelValF       =  1.                 ; max level
  res@cnLevelSpacingF      = .1                  ; contour level spacing

  lag                      = 0
  res@tiMainString         = "EnsembleSST vs HadISST Correlations ";" at lag "+lag xxxxxxx
  plot = gsn_csm_contour_map_ce(wks,ccr(:,:,lag),res) 
;************************************************
end






	
