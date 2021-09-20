FontUV='HOPS-164_cont_avg'

listobs(vis='HOPS-164.ms', listfile='HOPS-164.listobs.txt', verbose=True)

split(vis='HOPS-164.ms',
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
FontUV='HOPS-164_cont_avg'

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
FontUV='HOPS-164_cont_avg'

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
FontUV='HOPS-164_cont_avg'

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

tclean(vis= FontUV + '.Slfc3.ms',	# ['...12E', '...12W']
    imagename= FontUV + '.3',
    imsize= 512,
    cell= ['0.1arcsec'],
    field= '0',
    spw= '0,1,2',
    stokes= 'I',
    deconvolver= 'hogbom',
    weighting= 'briggs',
    robust= 0.5,
    gridder= 'standard',	# 'mosaic'
    datacolumn= 'data',
    specmode= 'mfs',
    pblimit=-1,	# 0.1
    mask= FontUV + '.2.mask',
    niter= 1000000,
    threshold= '0.008mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# peak: 
# noselfcal: 111.078 mJy,	1st selfcal: 115.732 mJy,	2nd_selfcal: 116.044 mJy,	3rd_selcal: 116.837 mJy

# rms:
# noselfcal: 0.184 mJy,	1st selfcal: 0.070 mJy,	2nd_selfcal: 0.069 mJy,	3rd_selcal: 0.067 mJy
    

#################################################### Stokes QUV #####################################################    
FontUV='HOPS-164_cont_avg'

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
# rms_StokesQ: 0.062		rms_StokesU: 0.062		rms_StokesQ: 0.062



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
    threshold= '0.124mJy',
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
    threshold= '0.124mJy',
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
    threshold= '0.124mJy',
    interactive= False,
    savemodel= 'modelcolumn')


# rms of 3rd_selfcal StokesQUV:
# rms_StokesQ: 0.061		rms_StokesU: 0.061		rms_StokesQ: 0.062


#################################################### POLI POLA RATIO #####################################################  
FontUV='HOPS-164_cont_avg'

immath(outfile=FontUV+'.POLI',
    mode='poli',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.0mJy/beam')
    
# POLI_rms: 0.087 mJy

# 'HOPS-164_cont_avg.POLA'['HOPS-164_cont_avg.POLI'>0.000261]

immath(outfile=FontUV+'.POLA',
    mode='pola',
    imagename=[FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    sigma='0.261mJy/beam')

immath(outfile=FontUV+'.RATIO',
    mode='evalexpr',
    imagename=[FontUV+'.3.image', FontUV+'.3.StokesQ.image', FontUV+'.3.StokesU.image'],
    expr='sqrt((IM1^2+IM2^2)/IM0[IM0>5e-3]^2)')






#################################################### uvcontsub #####################################################  
FontUV='HOPS-164_cont_avg'

split(vis='HOPS-164.ms',
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
    fitspw= '0:3~23, 0:26~28, 0:32~35, 0:39~44, 0:48~58, 0:60~61, 0:67~69, 0:74~80, 0:88~106, 0:125~137, 0:153~158, 0:161~164, 0:168~178, 0:197~202, 0:219~222, 0:226~228, 0:232~237, 0:240~243, 0:247~249, 0:252~257, 0:264~269, 0:272~274, 0:278~282, 0:298~305, 0:314~328, 0:332~337, 0:341~342, 0:353~355, 0:371~375, 0:388~390, 0:394~395, 0:400~401, 0:405~412, 0:415~424, 0:427~432, 0:436~440, 0:448~449, 0:455~456, 0:459~460, 0:470~472, 0:475~477, 0:492~503, 0:506~515, 0:518~530, 0:536~538, 0:549~551, 0:554~558, 0:561~565, 0:574~581, 0:589~590, 0:594~611, 0:615~620, 0:632~634, 0:656~662, 0:684~688, 0:695~696, 0:705~708, 0:724~726, 0:733~738, 0:746~747, 0:749~751, 0:804~806, 0:854~856, 0:1061~1062, 0:1072~1073, 0:1103~1104, 0:1109~1111, 0:1128~1129, 0:1139~1148, 0:1154~1160, 0:1171~1175, 0:1181~1182, 0:1241~1243, 0:1250~1255, 0:1260~1262, 0:1265~1272, 0:1288~1290, 0:1305~1307, 0:1322~1324, 0:1327~1333, 0:1351~1355, 0:1360~1364, 0:1378~1381, 0:1383~1384, 0:1396~1399, 0:1419~1421, 0:1425~1431, 0:1445~1453, 0:1458~1461, 0:1464~1467, 0:1471~1475, 0:1478~1480, 0:1487~1496, 0:1503~1516, 0:1520~1522, 0:1530~1536, 0:1543~1548, 0:1551~1562, 0:1567~1569, 0:1574~1577, 0:1582~1590, 0:1595~1597, 0:1627~1628, 0:1631~1635, 0:1638~1644, 0:1650~1653, 0:1660~1663, 0:1690~1692, 0:1695~1697, 0:1705~1709, 0:1721~1723, 0:1728~1732, 0:1780~1782, 0:1785~1791, 0:1798~1799, 0:1804~1806, 0:1811~1814, 0:1817~1821, 0:1824~1828, 0:1839~1843, 0:1875~1877, 0:1882~1884, 0:1888~1891, 0:1913~1919',
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
    chans= '750~970',      # Channels to use. Default is to use all channels
    outfile= 'moments0_750-970.image')
    
   
immoments(imagename= FontUV + '_CO32.selfcal.ms.contsub.final.image',
    moments=[0],      # integrated value of the spectrum
    axis= 'spectral',
    chans= '990~1190',      # Channels to use. Default is to use all channels
    outfile= 'moments0_990-1190.image')
    
# 'HOPS-164_cont_avg.POLA'['HOPS-164_cont_avg.POLI'>0.000261]
