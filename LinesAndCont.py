###################################################  START  ###################################################
##################################### identify bright lines and continuum #####################################
###############################################################################################################

FontUV=raw_input("Please input the source name: ")

#### split original data
print('\n' + "######## Split original data ......")
split(vis=FontUV+'.ms',
    spw='0,1,2,3',
    outputvis=FontUV+'.noflagging.ms',
    datacolumn='data')

      
#### apply selfcal solutions to the splitted data
print('\n' + "######## Apply selfcal solutions to the source ......")
applycal(vis=FontUV+'.noflagging.ms',
    gaintable= [FontUV+'.flaggedCO.slfcal.1', FontUV+'.flaggedCO.slfcal.2', FontUV+'.flaggedCO.slfcal.3'],
    calwt=False,
    applymode='calonly',
    spwmap=[0,1,2,3],
    flagbackup=False)


#### split the corrected data after apply selfcal solutions
print('\n' + "######## Split the data after applying selfcal solutions ......")
split(vis=FontUV+'.noflagging.ms',
    outputvis=FontUV+'.noflagging.selfcal.ms',
    datacolumn='corrected')


#### use tclean to make dirty cubes images for each spw to identify the channels of bright lines
print('\n' + "######## Make dirty cubes images for each spw ......")
tclean(vis=FontUV+'.noflagging.selfcal.ms',     
    imagename=FontUV+'.flagging_brightlines.selfcal.spw0.dirtycube',
    imsize=256,
    cell=['0.1arcsec'],
    spw='0',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)

tclean(vis=FontUV+'.noflagging.selfcal.ms',     
    imagename=FontUV+'.flagging_brightlines.selfcal.spw1.dirtycube',
    imsize=256,
    cell=['0.1arcsec'],
    spw='1',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
tclean(vis=FontUV+'.noflagging.selfcal.ms',     
    imagename=FontUV+'.flagging_brightlines.selfcal.spw2.dirtycube',
    imsize=256,
    cell=['0.1arcsec'],
    spw='2',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
tclean(vis=FontUV+'.noflagging.selfcal.ms',     
    imagename=FontUV+'.flagging_brightlines.selfcal.spw3.dirtycube',
    imsize=256,
    cell=['0.1arcsec'],
    spw='3',
    specmode='cube',
    stokes='I',
    deconvolver='hogbom',
    weighting='briggs',
    robust=0.5,
    pblimit=-1,
    niter=0,
    usemask='auto-multithresh',
    negativethreshold=0.0,
    interactive=False,
    gridder='standard',
    restoringbeam='common',
    chanchunks=-1)
    
    
    
os.system('rm -r '+FontUV+'.noflagging.ms')

###################################################   END   ###################################################
##################################### identify bright lines and continuum #####################################
###############################################################################################################

