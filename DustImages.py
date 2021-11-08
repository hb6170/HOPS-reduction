###################################################  START  ###################################################
############################################## flag bright lines ##############################################
###############################################################################################################


FontUV=raw_input("Please input the source name: ")


#### make a copy data for flagging bright lines
print('\n' + "######## Make a copy data for flagging bright lines ......")
os.system('cp -r '+FontUV+'.noflagging.selfcal.ms '+FontUV+'.flagging_brightlines.selfcal.ms')


Channels.bright_lines=raw_input("Please input the channels of bright lines: ")


#### flag the channels of bright lines of each spw
print('\n' + "######## Flag the channels of bright lines of each spw ......")
flagdata(vis=FontUV+'.flagging_brightlines.selfcal.ms',
    spw=Channels.bright_lines,
    flagbackup=False)


#### split the flagged data to run tclean more quickly
print('\n' + "######## Split the flagged data with channel_average to run tclean more quickly ......")
split(vis=FontUV+'.flagging_brightlines.selfcal.ms',
    spw='0,1,2,3',
    outputvis=FontUV+'.flagging_brightlines.selfcal_avgch.ms',
    width=[240,240,240,240],
    datacolumn='data')


#### use tclean to make images with Stokes IQUV, separately
print('\n' + "######## Use tclean to make images with Stokes IQUV ......")

calstat=imstat(imagename=FontUV + '.flaggedCO.3.image', stokes='I', region='', box='370,20,500,500')
rms_StokesI=(calstat['rms'][0])
threshold_StokesI="{:.3f}".format(2*rms_StokesI*1e3)+'mJy'
print '>> Threshold_StokesI: '+str(threshold_StokesI)

tclean(vis=FontUV+'.flagging_brightlines.selfcal_avgch.ms',
    imagename=FontUV+'.flagging_brightlines.selfcal_avgch.StokesI.finalmfs',
    imsize=512,
    cell=['0.1arcsec'],
    spw='0,1,2,3',
    specmode='mfs',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold=threshold_StokesI,  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)


calstat=imstat(imagename= FontUV + '.flaggedCO_StokesQ.3rd_selfcal.image', region='', box='370,20,500,500')
rms_tokesQ=(calstat['rms'][0])
threshold_StokesQ="{:.3f}".format(2*rms_StokesQ*1e3)+'mJy'
print '>> Threshold_StokesQ: '+str(threshold_StokesQ)

tclean(vis=FontUV+'.flagging_brightlines.selfcal_avgch.ms',
    imagename=FontUV+'.flagging_brightlines.selfcal_avgch.StokesQ.finalmfs',
    imsize=512,
    cell=['0.1arcsec'],
    spw='0,1,2,3',
    specmode='mfs',
    stokes='Q',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold=threshold_StokesQ,  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

calstat=imstat(imagename= FontUV + '.flaggedCO_StokesU.3rd_selfcal.image', region='', box='370,20,500,500')
rms_tokesU=(calstat['rms'][0])
threshold_StokesU="{:.3f}".format(2*rms_StokesU*1e3)+'mJy'
print '>> Threshold_StokesU: '+str(threshold_StokesU)

tclean(vis=FontUV+'.flagging_brightlines.selfcal_avgch.ms',
    imagename=FontUV+'.flagging_brightlines.selfcal_avgch.StokesU.finalmfs',
    imsize=512,
    cell=['0.1arcsec'],
    spw='0,1,2,3',
    specmode='mfs',
    stokes='U',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold=threshold_StokesU,  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    

calstat=imstat(imagename= FontUV + '.flaggedCO_StokesV.3rd_selfcal.image', region='', box='370,20,500,500')
rms_StokesV=(calstat['rms'][0])
threshold_StokesV="{:.3f}".format(2*rms_StokesV*1e3)+'mJy'
print '>> Threshold_StokesV: '+str(threshold_StokesV)

tclean(vis=FontUV+'.flagging_brightlines.selfcal_avgch.ms',
    imagename=FontUV+'.flagging_brightlines.selfcal_avgch.StokesV.finalmfs',
    imsize=512,
    cell=['0.1arcsec'],
    spw='0,1,2,3',
    specmode='mfs',
    stokes='V',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold=threshold_StokesV,  # 2sigma rms of 3rd_selfcal
    pblimit=-1,
    niter=1000000,
    usemask='auto-multithresh',
    sidelobethreshold=2.0,
    noisethreshold=4.25,
    lownoisethreshold=1.5,
    minbeamfrac=0.3,
    growiterations=75,
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)


#### make bright-line-flagged POLI, POLA and Pfrac images
print('\n' + "######## Make a copy data for flagging bright lines.")
immath(outfile=FontUV+'.flagging_brightlines.POLI',
    mode='poli',
    imagename=[FontUV+'.flagging_brightlines.selfcal_avgch.StokesQ.finalmfs.image', FontUV+'.flagging_brightlines.selfcal_avgch.StokesU.finalmfs.image'],
    sigma='0.0mJy/beam')

calstat=imstat(imagename= FontUV+'.flagging_brightlines.POLI', region='', box='370,20,500,500')
rms_POLI=(calstat['rms'][0])
sigma_POLI="{:.3f}".format(2*rms_POLI*1e3)+'mJy/beam'
print '>> Sigma_POLI: '+str(sigma_POLI)

immath(outfile=FontUV+'.flagging_brightlines.POLA',
    mode='pola',
    imagename=[FontUV+'.flagging_brightlines.selfcal_avgch.StokesQ.finalmfs.image', FontUV+'.flagging_brightlines.selfcal_avgch.StokesU.finalmfs.image'],
    sigma=sigma_POLI)

immath(outfile=FontUV+'.flagging_brightlines.RATIO',
    mode='evalexpr',
    imagename=[FontUV+'.flagging_brightlines.selfcal_avgch.StokesI.finalmfs.image', FontUV+'.flagging_brightlines.selfcal_avgch.StokesQ.finalmfs.image', FontUV+'.flagging_brightlines.selfcal_avgch.StokesU.finalmfs.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')


###################################################   END   ###################################################
############################################## flag bright lines ##############################################
###############################################################################################################
