import os
import sys


fw = open("Noise.txt", 'w')

###################################################   Pre   ###################################################
################################################### selfcal ###################################################
###############################################################################################################

#### source name
FontUV=raw_input("Please input the source name: ")
Solint1=raw_input("Please input the solint of first selfcal: ")
Solint2=raw_input("Please input the solint of second selfcal: ")
Solint3=raw_input("Please input the solint of third selfcal: ")


#### create a temparary copy of the source
print("Copy a temparary file of the source." + '\n')
os.system('cp -r ' + FontUV + '.ms tmp.ms')


#### Visually inspect amplitudes  vs.  frequency of the source in order to identify the channels of CO emission
print('\n' + "######## Plot spectrum of the source to identify the CO emission channels.")
plotms(vis=FontUV+'.ms',
    spw='0',
    xaxis='channel',
    yaxis='amp',
    avgtime='1e8',
    plotfile=FontUV+'_spectrum.png',
    iteraxis='spw',
    showgui=False)


#### Check if the continuun source is extended
#### Note the largest baseline in the plot in klambda 
#### we will need this information to set up the pixel scale of the image
plotms(vis=FontUV+'.ms',
    spw='',
    xaxis='uvwave',
    yaxis='amp',
    avgtime='1e8',
    avgchannel='1e8',
    iteraxis='spw',
    coloraxis='baseline',
    plotfile=FontUV+'_uvwave.png',
    showgui=False)


#### flag the channels of CO emission
print('\n' + "######## Now flag the CO emission channels.")
CO_emission_channels=raw_input("Please input the CO emission channels: ")
flagdata(vis='tmp.ms',
    spw=CO_emission_channels,
    flagbackup=False)

print('\n' + "######## Plot spectrum again to check the CO emission channels are indeed gone.")
plotms(vis=FontUV+'.ms',
    spw='0',
    xaxis='channel',
    yaxis='amp',
    avgtime='1e8',
    plotfile=FontUV+'_spectrum_flagged.png',
    iteraxis='spw',
    showgui=False)


#### split the flagged CO emission temparary source
print('\n' + "######## Split the temparary data.")
split(vis='tmp.ms',
    spw='0,1,2,3',
    outputvis=FontUV+'.flaggedCO.ms',
    width=[240,240,240,240],
    datacolumn='data')


#### make dirty image to check rms and peak value
print('\n' + "######## Use tclean to make dirty image to check noise and peak value.")
tclean(vis=FontUV+'.flaggedCO.ms',
    imagename=FontUV+'.flaggedCO_StokesI.noselfcal.dirty',
    spw='0,1,2,3',
    specmode='mfs',
    deconvolver='hogbom',
    stokes='I',
    gridder='standard',
    imsize=512,
    cell=['0.1arcsec'],
    weighting='briggs',
    robust=0.5,
    pblimit=-1,
    pbcor=True,
    niter=0,
    interactive=False,
    savemodel='modelcolumn')

#### obtain the rms, peak, SNR value
print('\n' + "######## Noise, Peak and SNR in pre_selfcal are: ")
calstat=imstat(imagename=FontUV+'.flaggedCO_StokesI.noselfcal.dirty.image', stokes='I', region='', box='370,20,500,500')
rms_preselfcal=(calstat['rms'][0])
rms0=2*rms_preselfcal*1e3
threshold_preselfcal="{:.3f}".format(rms0)+'mJy'
print '>> rms_preselfcal in continuum image: '+str(rms_preselfcal*1e3)+' mJy'
print '>> threshold_preselfcal: '+str(threshold_preselfcal)
calstat=imstat(imagename=FontUV+'.flaggedCO_StokesI.noselfcal.dirty.image', region='')
peak_preselfcal=(calstat['max'][0])
print '>> Peak_preselfcal in continuum image: '+str(peak_preselfcal*1e3)+' mJy'
print '>> Dynamic range of preselfcal in continuum image: '+str(peak_preselfcal/rms_preselfcal)+'\n'


#### use tclean to make image for selfcal
print('\n' + "######## Preperation tclean for selfcal.")
tclean(vis=FontUV+'.flaggedCO.ms',
    imagename=FontUV+'.flaggedCO_StokesI.noselfcal',
    spw='0,1,2,3',
    specmode='mfs',
    deconvolver='hogbom',
    stokes='I',
    gridder='standard',
    imsize=512,
    cell=['0.1arcsec'],
    weighting='briggs',
    robust=0.5,
    threshold=threshold_preselfcal,
    pblimit=-1,
    pbcor=True,
    niter=1000000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive=False,
    savemodel='modelcolumn')



###################################################  START  ###################################################
################################################### selfcal ###################################################
###############################################################################################################

################################################# 1st selfcal #################################################
print('\n' + "######## First selfcal steps ......")
gaincal(vis=FontUV+'.flaggedCO.ms',
    caltable=FontUV+'.flaggedCO.slfcal.1',
    refant='DA43',
    spw='0,1,2,3',
    gaintype='T',
    calmode='p',
    solint=Solint1)

plotcal(caltable=FontUV+'.flaggedCO.slfcal.1',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=False,
    figfile='Gain_'+FontUV+'.flaggedCO.slfcal1.png')
    
applycal(vis=FontUV+'.flaggedCO.ms',
    gaintable=FontUV+'.flaggedCO.slfcal.1',
    calwt=False,
    applymode='calonly',
    flagbackup=False)

split(vis=FontUV+'.flaggedCO.ms',
    outputvis=FontUV+'.flaggedCO.Slfc1.ms',
    datacolumn='corrected')


#### use tclean to make images of 1st selfcal
tclean(vis= FontUV + '.flaggedCO.Slfc1.ms',
    imagename= FontUV + '.flaggedCO.1',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    niter= 1000000,
    threshold= '0.03mJy',
    interactive= False,
    savemodel= 'modelcolumn')
   

#### obtain the rms, peak, SNR value of 1st_selfcal
print('\n' + "######## Noise, Peak and SNR in the first selfcal are: ")
calstat=imstat(imagename=FontUV + '.flaggedCO.1.image', stokes='I', region='', box='370,20,500,500')
rms_1st_selfcal=(calstat['rms'][0])
rms1=2*rms_1st_selfcal*1e3
threshold_1st_selfcal="{:.3f}".format(rms1)+'mJy'
print '>> rms_1st_selfcal in continuum image: '+str(rms_1st_selfcal*1e3)+' mJy'
print '>> threshold_1st_selfcal: '+str(threshold_1st_selfcal)
calstat=imstat(imagename=FontUV + '.flaggedCO.1.image', region='')
peak_1st_selfcal=(calstat['max'][0])
print '>> Peak_1st_selfcal in continuum image: '+str(peak_1st_selfcal*1e3)+' mJy'
print '>> Dynamic range of 1st_selfcal in continuum image: '+str(peak_1st_selfcal/rms_1st_selfcal)+'\n'


################################################# 2nd selfcal #################################################
print('\n' + "######## Second selfcal steps ......")
gaincal(vis=FontUV+'.flaggedCO.Slfc1.ms',
    caltable=FontUV+'.flaggedCO.slfcal.2',
    refant='DA43',
    spw='0,1,2,3',
    gaintype='T',
    calmode='p',
    solint=Solint1)

plotcal(caltable=FontUV+'.flaggedCO.slfcal.2',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=False,
    figfile='Gain_'+FontUV+'.flaggedCO_slfcal2.png')
    
applycal(vis=FontUV+'.flaggedCO.Slfc1.ms',
    gaintable=FontUV+'.flaggedCO.slfcal.2',
    calwt=False,
    applymode='calonly',
    flagbackup=False)

split(vis=FontUV+'.flaggedCO.Slfc1.ms',
    outputvis=FontUV+'.flaggedCO.Slfc2.ms',
    datacolumn='corrected')


#### use tclean to make images of 2nd selfcal
tclean(vis= FontUV + '.flaggedCO.Slfc2.ms',
    imagename= FontUV + '.flaggedCO.2',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    niter= 1000000,
    threshold= '0.01mJy',
    interactive= False,
    savemodel= 'modelcolumn')


#### obtain the rms, peak, SNR value of 2nd_selfcal
print('\n' + "######## Noise, Peak and SNR in the second selfcal are: ")
calstat=imstat(imagename=FontUV + '.flaggedCO.2.image', stokes='I', region='', box='370,20,500,500')
rms_2nd_selfcal=(calstat['rms'][0])
rms2=2*rms_2nd_selfcal*1e3
threshold_2nd_selfcal="{:.3f}".format(rms2)+'mJy'
print '>> rms_2nd_selfcal in continuum image: '+str(rms_2nd_selfcal*1e3)+' mJy'
print '>> threshold_2nd_selfcal: '+str(threshold_2nd_selfcal)
calstat=imstat(imagename=FontUV + '.flaggedCO.2.image', region='')
peak_2nd_selfcal=(calstat['max'][0])
print '>> Peak_2nd_selfcal in continuum image: '+str(peak_2nd_selfcal*1e3)+' mJy'
print '>> Dynamic range of 2nd_selfcal in continuum image: '+str(peak_2nd_selfcal/rms_2nd_selfcal)+ '\n'

################################################# 3rd selfcal #################################################
print('\n' + "######## Third selfcal steps ......")
gaincal(vis=FontUV+'.flaggedCO.Slfc2.ms',
    caltable=FontUV+'.flaggedCO.slfcal.3',
    refant='DA43',
    spw='0,1,2,3',
    gaintype='T',
    calmode='p',
    solint=Solint1)

plotcal(caltable=FontUV+'.flaggedCO.slfcal.3',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=False,
    figfile='Gain_'+FontUV+'.flaggedCO_slfcal3.png')
    
applycal(vis=FontUV+'.flaggedCO.Slfc2.ms',
    gaintable=FontUV+'.flaggedCO.slfcal.3',
    calwt=False,
    applymode='calonly',
    flagbackup=False)

split(vis=FontUV+'.flaggedCO.Slfc2.ms',
    outputvis=FontUV+'.flaggedCO.Slfc3.ms',
    datacolumn='corrected')


#### use tclean to make images of 3rd selfcal
tclean(vis= FontUV + '.flaggedCO.Slfc3.ms',
    imagename= FontUV + '.flaggedCO.3',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    niter= 1000000,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')


#### obtain the rms, peak, SNR value of 3rd_selfcal
print('\n' + "######## Noise, Peak and SNR in the third selfcal are: ")
calstat=imstat(imagename=FontUV + '.flaggedCO.3.image', stokes='I', region='', box='370,20,500,500')
rms_3rd_selfcal=(calstat['rms'][0])
rms3=2*rms_3rd_selfcal*1e3
threshold_3rd_selfcal="{:.3f}".format(rms3)+'mJy'
print '>> rms_3rd_selfcal in continuum image: '+str(rms_3rd_selfcal*1e3)+' mJy'
print '>> threshold_3rd_selfcal: '+str(threshold_3rd_selfcal)
calstat=imstat(imagename=FontUV + '.flaggedCO.3.image', region='')
peak_3rd_selfcal=(calstat['max'][0])
print '>> Peak_3rd_selfcal in continuum image: '+str(peak_3rd_selfcal*1e3)+' mJy'
print '>> Dynamic range of 3rd_selfcal in continuum image: '+str(peak_3rd_selfcal/rms_3rd_selfcal)+ '\n'


########################################## Stokes QVU in 3rd selfcal ##########################################
tclean(vis= FontUV + '.flaggedCO.Slfc3.ms',
    imagename= FontUV + '.flaggedCO_StokesQ.3rd_selfcal.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    niter= 0,
    interactive= False,
    savemodel= 'modelcolumn')
    
print('\n' + "######## Noise of the third selfcal dirty image with StokesQ is: ")
calstat=imstat(imagename= FontUV + '.flaggedCO_StokesQ.3rd_selfcal.dirty.image', region='', box='370,20,500,500')
rms_3rd_selfcal_StokesQ_dirty=(calstat['rms'][0])
rmsQ_dirty=2*rms_3rd_selfcal_StokesQ_dirty*1e3
threshold_StokesQ_dirty="{:.3f}".format(rmsQ_dirty)+'mJy'
print '>> rms_3rd_selfcal_StokesQ in dirty image: '+str(rms_3rd_selfcal_StokesQ_dirty*1e3)+' mJy'
print '>> threshold_3rd_selfcal_StokesQ in dirty image: '+str(threshold_StokesQ_dirty)+ '\n'


tclean(vis= FontUV + '.flaggedCO.Slfc3.ms',
    imagename= FontUV + '.flaggedCO_StokesQ.3rd_selfcal',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    threshold=threshold_StokesQ_dirty,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=4.25,
    niter= 1000000,
    interactive= False,
    savemodel= 'modelcolumn')

## obtain rms value for the threshold in the tclean with StokesQ
print('\n' + "######## Noise of the third selfcal with StokesQ is: ")
calstat=imstat(imagename= FontUV + '.flaggedCO_StokesQ.3rd_selfcal.image', region='', box='370,20,500,500')
rms_3rd_selfcal_StokesQ=(calstat['rms'][0])
print '>> rms_3rd_selfcal_StokesQ: '+str(rms_3rd_selfcal_StokesQ*1e3)+' mJy'


tclean(vis= FontUV + '.flaggedCO.Slfc3.ms',
    imagename= FontUV + '.flaggedCO_StokesU.3rd_selfcal.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    niter= 0,
    interactive= False,
    savemodel= 'modelcolumn')

## obtain rms value for the threshold in the tclean with StokesU
print('\n' + "######## Noise of the third selfcal dirty image with StokesU is: ")
calstat=imstat(imagename= FontUV + '.flaggedCO_StokesU.3rd_selfcal.dirty.image', region='', box='370,20,500,500')
rms_3rd_selfcal_StokesU_dirty=(calstat['rms'][0])
rmsU_dirty=2*rms_3rd_selfcal_StokesU_dirty*1e3
threshold_StokesU_dirty="{:.3f}".format(rmsU_dirty)+'mJy'
print '>> rms_3rd_selfcal_StokesU in dirty image: '+str(rms_3rd_selfcal_StokesU_dirty*1e3)+' mJy'
print '>> threshold_3rd_selfcal_StokesU in dirty image: '+str(threshold_StokesU_dirty)+ '\n'

tclean(vis= FontUV + '.flaggedCO.Slfc3.ms',
    imagename= FontUV + '.flaggedCO_StokesU.3rd_selfcal',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    threshold=threshold_StokesU_dirty,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=4.25,
    niter= 1000000,
    interactive= False,
    savemodel= 'modelcolumn')

## obtain rms value for the threshold in the tclean with StokesU
print('\n' + "######## Noise of the third selfcal with StokesU is: ")
calstat=imstat(imagename= FontUV + '.flaggedCO_StokesU.3rd_selfcal.image', region='', box='370,20,500,500')
rms_3rd_selfcal_StokesU=(calstat['rms'][0])
print '>> rms_3rd_selfcal_StokesU: '+str(rms_3rd_selfcal_StokesU*1e3)+' mJy'


tclean(vis= FontUV + '.flaggedCO.Slfc3.ms',
    imagename= FontUV + '.flaggedCO_StokesV.3rd_selfcal.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    niter= 0,
    interactive= False,
    savemodel= 'modelcolumn')
    
## obtain rms value for the threshold in the tclean with StokesV
print('\n' + "######## Noise of the third selfcal dirty image with StokesV is: ")
calstat=imstat(imagename= FontUV + '.flaggedCO_StokesV.3rd_selfcal.dirty.image', region='', box='370,20,500,500')
rms_3rd_selfcal_StokesV_dirty=(calstat['rms'][0])
rmsV_dirty=2*rms_3rd_selfcal_StokesV_dirty*1e3
threshold_StokesV_dirty="{:.3f}".format(rmsV_dirty)+'mJy'
print '>> rms_3rd_selfcal_StokesV in dirty image: '+str(rms_3rd_selfcal_StokesV_dirty*1e3)+' mJy'
print '>> threshold_3rd_selfcal_StokesV in dirty image: '+str(threshold_StokesV_dirty)+ '\n'

    
tclean(vis= FontUV + '.flaggedCO.Slfc3.ms',
    imagename= FontUV + '.flaggedCO_StokesV.3rd_selfcal',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2,3',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    threshold=threshold_StokesV_dirty,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=4.25,
    niter= 1000000,
    interactive= False,
    savemodel= 'modelcolumn')

## obtain rms value for the threshold in the tclean with StokesV
print('\n' + "######## Noise of the third selfcal with StokesV is: ")
calstat=imstat(imagename= FontUV + '.flaggedCO_StokesV.3rd_selfcal.image', region='', box='370,20,500,500')
rms_3rd_selfcal_StokesV=(calstat['rms'][0])
print '>> rms_3rd_selfcal_StokesV: '+str(rms_3rd_selfcal_StokesV*1e3)+' mJy'


fw.write("pre_selfcal: "+"\n"+"rms: "+str(rms_preselfcal*1e3)+" mJy"+"\t"+"peak: "+str(peak_preselfcal*1e3)+" mJy"+"\t"+"SNR: "+str(peak_preselfcal/rms_preselfcal)+"\n"+"\n")
fw.write("1st_selfcal: "+"\n"+"rms: "+str(rms_1st_selfcal*1e3)+" mJy"+"\t"+"peak: "+str(peak_1st_selfcal*1e3)+" mJy"+"\t"+"SNR: "+str(peak_1st_selfcal/rms_1st_selfcal)+"\n"+"\n")
fw.write("2nd_selfcal: "+"\n"+"rms: "+str(rms_2nd_selfcal*1e3)+" mJy"+"\t"+"peak: "+str(peak_2nd_selfcal*1e3)+" mJy"+"\t"+"SNR: "+str(peak_2nd_selfcal/rms_2nd_selfcal)+"\n"+"\n")
fw.write("3rd_selfcal: "+"\n"+"rms: "+str(rms_3rd_selfcal*1e3)+" mJy"+"\t"+"peak: "+str(peak_3rd_selfcal*1e3)+" mJy"+"\t"+"SNR: "+str(peak_3rd_selfcal/rms_3rd_selfcal)+"\n"+"\n")
fw.write("3rd_selfcal_StokesQ: "+"\n"+"rms: "+str(rms_3rd_selfcal_StokesQ*1e3)+" mJy"+"\n"+"\n")
fw.write("3rd_selfcal_StokesU: "+"\n"+"rms: "+str(rms_3rd_selfcal_StokesU*1e3)+" mJy"+"\n"+"\n")
fw.write("3rd_selfcal_StokesV: "+"\n"+"rms: "+str(rms_3rd_selfcal_StokesV*1e3)+" mJy")


os.system('rm -r tmp.ms')

fw.close()


###################################################   END   ###################################################
################################################### selfcal ###################################################
###############################################################################################################
