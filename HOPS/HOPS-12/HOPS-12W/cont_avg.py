FontUV='HOPS-12W_cont_avg'

listobs(vis='HOPS-12W.ms', listfile='HOPS-12W.listobs.txt', verbose=True)

split(vis='HOPS-12W.ms',
    spw='1,2,3',
    outputvis=FontUV+'.ms',
    width=[240,240,240],
    datacolumn='data')

tclean(vis=FontUV+'.ms',
    imagename=FontUV+'.StokesI_noselfcal.tclean',
    spw='0,1,2',
    specmode='mfs',
    deconvolver='hogbom',
    stokes='I',
    gridder='standard',
    imsize=512,
    cell=['0.1arcsec'],
    weighting='briggs',
    robust=0.5,
    threshold='0.0mJy',
    pblimit=-1,
    pbcor=False,
    niter=1000000,
    interactive=True,
    savemodel='modelcolumn')
    
    
#################################################### 1st selfcal #####################################################
FontUV='HOPS-12W_cont_avg'

gaincal(vis=FontUV+'.ms',
    caltable=FontUV+'.slfcal.1',
    refant='DA43',
    spw='0,1,2',
    gaintype='T',
    calmode='p',
    solint='600s')

plotcal(caltable=FontUV+'.slfcal.1',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'_slfcal1.png')
    
applycal(vis=FontUV+'.ms',
    gaintable=FontUV+'.slfcal.1',
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2],
    flagbackup=False)

split(vis=FontUV+'.ms',
    outputvis=FontUV+'.Slfc1.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.Slfc1.ms',
    imagename= FontUV + '.1',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.StokesI_noselfcal.tclean.mask',
    niter= 1000000,
    threshold= '0.0mJy',
    interactive= True,
    savemodel= 'modelcolumn')


#################################################### 2nd selfcal #####################################################
FontUV='HOPS-12W_cont_avg'

gaincal(vis=FontUV+'.Slfc1.ms',
    caltable=FontUV+'.slfcal.2',
    refant='DA43',
    spw='0,1,2',
    gaintype='T',
    calmode='p',
    solint='30s')

plotcal(caltable=FontUV+'.slfcal.2',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'_slfcal2.png')
    
applycal(vis=FontUV+'.Slfc1.ms',
    gaintable=FontUV+'.slfcal.2',
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2],
    flagbackup=False)

split(vis=FontUV+'.Slfc1.ms',
    outputvis=FontUV+'.Slfc2.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.Slfc2.ms',
    imagename= FontUV + '.2',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.1.mask',
    niter= 1000000,
    threshold= '0.0mJy',
    interactive= True,
    savemodel= 'modelcolumn')
    
    
    
#################################################### 3rd selfcal #####################################################
FontUV='HOPS-12W_cont_avg'

gaincal(vis=FontUV+'.Slfc2.ms',
    caltable=FontUV+'.slfcal.3',
    refant='DA43',
    spw='0,1,2',
    gaintype='T',
    calmode='p',
    solint='10s')

plotcal(caltable=FontUV+'.slfcal.3',
    xaxis='time',
    yaxis='phase',
    plotrange=[0,0,-180,180],
    plotsymbol='o-',
    iteration='antenna',
    subplot=431,
    showgui=True,
    figfile='Gain_'+FontUV+'_slfcal3.png')
    
applycal(vis=FontUV+'.Slfc2.ms',
    gaintable=FontUV+'.slfcal.3',
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2],
    flagbackup=False)

split(vis=FontUV+'.Slfc2.ms',
    outputvis=FontUV+'.Slfc3.ms',
    datacolumn='corrected')

tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.2.mask',
    niter= 1000000,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# peak: 
# noselfcal: 89.536 mJy,	1st selfcal: 96.206 mJy,	2nd_selfcal: 96.445 mJy,	3rd_selcal: 97.372 mJy

# rms:
# noselfcal: 0.282 mJy,	1st selfcal: 0.101 mJy,	2nd_selfcal: 0.099 mJy,	3rd_selcal: 0.091 mJy
    

#################################################### Stokes QUV #####################################################    
FontUV='HOPS-12W_cont_avg'

tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesQ.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 0,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesU.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 0,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesV.dirty',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 0,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')

# rms of dirty StokesQUV:
# rms_StokesQ: 0.078		rms_StokesU: 0.079		rms_StokesQ: 0.079



tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesQ',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'Q',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 1000000,
    threshold= '0.156mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesU',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'U',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 1000000,
    threshold= '0.158mJy',
    interactive= False,
    savemodel= 'modelcolumn')
    
tclean(vis= FontUV + '.Slfc3.ms',
    imagename= FontUV + '.3.StokesV',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'V',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,
    mask= FontUV + '.3.mask',
    niter= 1000000,
    threshold= '0.158mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# rms of 3rd_selfcal StokesQUV:
# rms_StokesQ: 0.077		rms_StokesU: 0.079		rms_StokesQ: 0.079


#################################################### POLI POLA RATIO #####################################################  
FontUV='HOPS-12W_cont_avg'

immath(outfile=FontUV+'.POLI',
    mode='poli',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.0mJy/beam')
    
# POLI_rms: 0.11 mJy

# 'HOPS-12W_cont_avg.POLA'['HOPS-12W_cont_avg.POLI'>0.00033]

immath(outfile=FontUV+'.POLA',
    mode='pola',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.33mJy/beam')

immath(outfile=FontUV+'.RATIO',
    mode='evalexpr',
    imagename=[FontUV+'.3.image', FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')






#################################################### uvcontsub #####################################################  
FontUV='HOPS-12W_cont_avg'

split(vis='HOPS-12W.ms',
    field='0',
    spw='0',
    outputvis= FontUV + '_CO32.ms',
    datacolumn='data')
    
applycal(vis = FontUV+'_CO32.ms',
    gaintable= [FontUV+'.slfcal.1', FontUV+'.slfcal.2', FontUV+'.slfcal.3'],
    calwt= False,
    applymode= 'calonly',
    spwmap=[0],
    flagbackup= False)
    
split(vis = FontUV + '_CO32.ms',
    outputvis= FontUV + '_CO32.selfcal.ms',
    datacolumn= 'corrected')

delmod(vis= FontUV + '_CO32.selfcal.ms')
    
tclean(vis=FontUV+'_CO32.selfcal.ms',     
    imagename=FontUV+'_CO32.selfcal.dirty',
    imsize=256,
    cell=['0.1arcsec'],
    field='0',
    spw='0',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    threshold='0.184mJy',
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

uvcontsub(vis= FontUV + '_CO32.selfcal.ms',
    spw= '0',             # spw to do continuum subtraction on
    fitspw= '0:1~22, 0:38~45, 0:68~174, 0:180~185, 0:193~201, 0:221~260, 0:266~350, 0:385~391, 0:398~402, 0:413~422, 0:427~458, 0:465~478, 0:484~499, 0:505~509, 0:513~522, 0:528~530, 0:533~534, 0:554~556, 0:559~568, 0:571~578, 0:589~591, 0:595~598, 0:602~608, 0:613~616, 0:619~625, 0:629~637, 0:684~686, 0:698~702, 0:719~720, 0:723~725, 0:1107~1108, 0:1116~1125, 0:1130~1145, 0:1148~1162, 0:1164~1179, 0:1183~1212, 0:1215~1218, 0:1229~1283, 0:1288~1299, 0:1302~1304, 0:1315~1321, 0:1339~1354, 0:1357~1360, 0:1364~1371, 0:1386~1397, 0:1430~1433, 0:1435~1437, 0:1453~1470, 0:719~720, 0:723~725, 0:1107~1108, 0:1116~1125, 0:1130~1145, 0:1148~1162, 0:1164~1179, 0:1183~1212, 0:1215~1218, 0:1497~1502, 0:1506~1509, 0:1514~1525, 0:1545~1553, 0:1562~1572, 0:1577~1582, 0:1594~1596, 0:1599~1609, 0:1614~1619, 0:1622~1632, 0:1635~1668, 0:1672~1677, 0:1683~1721, 0:1733~1736, 0:1741~1744, 0:1754~1769, 0:1783~1799, 0:1807~1812, 0:1825~1911',
    excludechans= False,          # fit the region in fitspw
    solint= 'int',             # no time averaging, do a fit for each integration and let the noise fits average out in the image
    fitorder= 1,            # polynomial order for the fits of the continuum
    want_cont= False)        # create vis+'.contsub' to hold the continuum estimate

delmod(vis= FontUV + '_CO32.selfcal.ms.contsub')

tclean(vis= FontUV + '_CO32.selfcal.ms.contsub',
    imagename= FontUV + '_CO32.selfcal.ms.contsub.dirty',
    imsize= 256,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    threshold= '0.008mJy',     # the same as 3rd selfcal, 2sigma
    pblimit= -1,
    niter= 0,
    usemask='auto-multithresh',
    negativethreshold=0.0,    # the 75th percentile of baselines >300m
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)

tclean(vis= FontUV + '_CO32.selfcal.ms.contsub',
    imagename= FontUV + '_CO32.selfcal.ms.contsub.final',
    imsize= 256,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0',
    specmode= 'cube',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    pbcor= True,      # apply pb correlation on the output restored image
    threshold= '0.008mJy',     # the same as 3rd selfcal, 2sigma
    pblimit= -1,
    niter= 100000,
    usemask='auto-multithresh',
    negativethreshold=0.0,    # the 75th percentile of baselines >300m
    interactive= False,
    gridder= 'standard',      # prolate spheroid with 7*7 pixel support size
    restoringbeam='common',    #  Automatically estimate a common beam shape/size appropriate for all planes
    chanchunks=-1)            # break up large cubes automatically so that you don't run out of memory


immoments(imagename= FontUV + '_CO32.selfcal.ms.contsub.final.image',
    moments=[0],      # integrated value of the spectrum
    axis= 'spectral',
    chans= '750~956',      # Channels to use. Default is to use all channels
    outfile= 'moments0_750-956.image')
    
   
immoments(imagename= FontUV + '_CO32.selfcal.ms.contsub.final.image',
    moments=[0],      # integrated value of the spectrum
    axis= 'spectral',
    chans= '983~1170',      # Channels to use. Default is to use all channels
    outfile= 'moments0_983-1170.image')
    
# 'HOPS-12W_cont_avg.POLA'['HOPS-12W_cont_avg.POLI'>0.00033]
