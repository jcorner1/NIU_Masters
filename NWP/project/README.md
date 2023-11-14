# Final Project

## Methods

### Physics Schemes

### Namelists
The sections provides the namelist.iput to show the various settings used in the project:


## Running WRF Steps
This outline is not meant to go into great detail on how to run the WRF, but rather a simplistic overview of the basic steps. 
* <a href="https://github.com/jcorner1/NIU_Masters/blob/main/NWP/project/Files/geogrid.job">Geogrid</a> - Create Geographical data for WRF
  * <a href="https://jiririchter.github.io/WRFDomainWizard/">Domain Wizard</a> - GitHub page for creating Geogrid domain
* Ungrib - 
  * <a href="https://github.com/jcorner1/NIU_Masters/blob/main/NWP/project/Files/link_grib.csh">linkgrib.csh</a> - Link files in format readable to ungrib
* <a href="https://github.com/jcorner1/NIU_Masters/blob/main/NWP/project/Files/metgrid.job">Metgrid</a> - 
* <a href="https://github.com/jcorner1/NIU_Masters/blob/main/NWP/project/Files/real.job">Real.job</a> - 
* <a href="https://github.com/jcorner1/NIU_Masters/blob/main/NWP/project/Files/wrf.job">WRF.exe</a> - Running the WRF

Finally, an outline with a bit more detail can be found <a href="https://docs.google.com/document/d/1LsTXlVE2OE-Uov-DA3PnJBMGP3Ji-BraFDcpkfGKr4k/edit?usp=drive_link">here</a> and the diagram below should hopefully provide a basic visual of the process. 
<p>
    <img src="https://github.com/jcorner1/NIU_Masters/blob/main/NWP/project/Plots/WRF-algorithm-workflow-diagram.png" width="617" height="347" />
</p>

