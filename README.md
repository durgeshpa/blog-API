### Wind_325 Split Documentation

**Date:** 2024-09-30  
**Project:** Wind_325 Split  
**Note:** The following changes must be implemented carefully on production systems. Key differences in production:

1. **repconfig.xml updates**:
   - Update `repconfig.xml` on four servers (two per bay), which all access the same database.
   - Be mindful of the `&` issue in XML (consult Christian or Felix if uncertain).
  
2. **ICNOC API Import**:
   - Use the following paths for ICNOC API import:  
     - `d:\Anemos\bin\importer\icnoc-import\`  
     - `d:\Anemos\var\data\meas-import\icnoc\`  
   - Note: `site.json` does not contain sites currently imported via SFTP.

### Step-by-Step Instructions:

#### Step 1: Server 01

1. **Config Backup:**
   - Backup the entire config folder using Total Commander (shortcut: `Alt+F5`).
  
2. **Update repconfig.xml:**
   - Copy `repconfig.xml` from the Bay 1 server to the `oamdm` folder on the Bay 2 server.
   - Add Wind_325 clusters from the Bay 1 `repconfig.xml` to the existing `repconfig.xml` on the Bay 2 server.

#### Step 2: Server 02

1. **repconfig.xml Update:**
   - Copy `d:\Anemos\config\tsdr\repconfig.xml` from Server 01 to Server 02.
   - Make a backup and use a diff tool to verify changes.

2. **Restart Tomcat Service:**
   - Restart the Tomcat service through Windows Services.

#### Step 3: Server 03

1. **SCADA Import Configuration:**
   - Insert `ApplicationWindFarm` elements for 3 new sites into `Adani.csv-meas-import-wind-icnoc.xml`.
   - Copy `ApplicationParameters` from Wind_325 to the 3 new sites.
   - Insert new lines into the `site.json` file based on the turbine IDs for the new sites.
   - Insert sections for the new sites into the `preproc.rename-copy-scada-files-wind-icnoc.pl` script.

2. **Check Operational SCADA Import:**
   - Verify the SCADA import process for the new sites to ensure correct data processing.

3. **NWP Import Configuration:**
   - Update the following files in `d:\Anemos\config\sdrxml`:
     - `Adani.ecmwf-grib-import-0012.xml`
     - `Adani.ecmwf-grib-import-0618.xml`
     - `Adani.gfs-grib-import.xml`
     - `Adani.ncmrwf-grib-import-00.xml`
     - `Adani.ncmrwf-grib-import-12.xml`
   - Copy `ApplicationWindFarm` elements from the updated XML files and paste them into the operational XML files.

4. **Re-run NWP Imports:**
   - Re-run the latest NWP import using the following commands:
     - For ECMWF:  
       ```shell
       /cygdrive/d/Anemos/bin/amwrapper/amwrapper.pl -L routine Adani ecmwf_oshybrid-wind-py 2024-06-28T00:00:00
       ```
     - For NCMRWF:  
       ```shell
       /cygdrive/d/Anemos/bin/amwrapper/amwrapper.pl -L routine Adani ncmrwf_oshybrid-wind-py 2024-06-27T00:00:00
       ```
   - For both imports, check the logs in `d:\Anemos\var\log\ecmwf-chain\` or `d:\Anemos\var\log\ncmrwf-chain\`.

5. **Dayahead/Weekahead Forecasting Models:**
   - Copy the 3 new sites to the following XML files:
     - `Adani.nwp-interpolation.xml`
     - `Adani.ecmwf_oshybrid-wind-py.xml`
     - `Adani.ncmrwf_oshybrid-wind-py.xml`
     - `Adani.combination-wind-from-py.xml`
     - `Adani.combination_postproc-wind-from-py.xml`
   - Copy the prepared `Wind_325_c1/2/3.siteconfig.json` files to:
     - `d:\Anemos\var\storage\ecmwf_oshybrid-wind-py\siteconfig\wind\`
     - `d:\Anemos\var\storage\ncmrwf_oshybrid-wind-py\siteconfig\wind\`

6. **Create Configuration Files:**
   - Create `*.Run.cfg` files for `Wind_325_c1/2/3` in `d:\Anemos\var\storage\nwp-interpolation\` based on Wind_325, modifying only the name in the filename and `Location$Name` inside the files.

7. **Update and Re-run Connector Scripts:**
   - Add 3 new sites to the connector script:
     - `d:\Anemos\bin\modules-wrapped\nwp-interpolation\source\bin\connector_nwp-interpolation.pl`
   - Re-run the latest operational NWP interpolation run with `-L` option to avoid logging:
     ```shell
     /cygdrive/d/Anemos/bin/amwrapper/amwrapper.pl -L routine Adani nwp-interpolation 2024-06-28T00:00:00
     ```

8. **Intraday Forecasting Models:**
   - Copy the 3 new sites to:
     - `Adani.osdyn-wind-py.xml`
     - `Adani.dynamic_postproc-wind-from-py.xml`
   - Update the connector script:
     - `d:\Anemos\bin\modules-wrapped\osdyn-wind-py\source\bin\connector_osdyn-wind-py.pl`

9. **Re-run Intraday Forecasting:**
   - Re-run the latest operational `osdyn-wind-py` run:
     ```shell
     /cygdrive/d/Anemos/bin/amwrapper/amwrapper.pl -L routine Adani osdyn-wind-py 2024-06-28T09:45:00
     ```
   - Re-run the `dynamic_postproc-wind-from-py` run:
     ```shell
     /cygdrive/d/Anemos/bin/amwrapper/amwrapper.pl -L routine Adani dynamic_postproc-wind-from-py 2024-06-28T09:45:00
     ```

10. **Forecast Export Configuration:**
    - Add 3 new sites to:
      - `d:\Anemos\config\sdrxml\Adani.wpp-export-wind-all.xml`
      - `d:\Anemos\config\sdrxml\Adani.wpp-export-wind-ctu.xml`
    - Check the next intraday CTU export or verify through the GUI.

#### Step 4: Server 04

1. **Config Backup:**
   - Backup the config folder.

2. **Master Table Update:**
   - Backup `d:\Anemos\config\sofa\master-table\Adani.farm-static-data.current.tsv`.
   - Copy the updated `Adani.farm-static-data.current.tsv` to `d:\Anemos\config\sofa\master-table`.

3. **Static Plots Configuration:**
   - Add 3 new sites to:
     - `d:\Anemos\config\sdrxml\Adani.static-plots-dayahead.xml`
     - `d:\Anemos\config\sdrxml\Adani.static-plots-intraday.xml`

4. **GUI Update:**
   - Add 3 new sites to `d:\Anemos\config\anemosliveweb\Adani.anemosliveweb.xml`.
   - Restart the Tomcat service.
   - Check the GUI to confirm that new sites are visible (may require re-login).

---

### Final Checks

- Ensure that all services are restarted, and configurations are correctly applied.
- Verify that new sites appear in the SCADA, NWP, intraday forecasts, and GUI.
- Re-run test imports and forecasts for validation before marking the update as complete.
- Re-run test imports and forecasts for validation before marking the update as complete.
