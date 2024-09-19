Here is an even more detailed breakdown of the onboarding process for a new solar site like AGE25L:

---

# **Onboarding a New Solar Site - Step-by-Step Detailed Guide**

---

## **1. Update the Master Table**
   - **Purpose**: Ensure that the master table reflects the addition of the new site and its metadata.
   - **Location**: Master Excel file (sofa table).
   - **Steps**:
     1. **Open the master Excel file**: Locate the most recent master table Excel file.
     2. **Enter new site details**:
        - **Site name**: AGE25L
        - **Coordinates**: Latitude, Longitude
        - **Power Capacity**: Input the new site’s rated power.
        - **Other metadata**: Include site-specific details such as region, operator, and commissioning date.
     3. **Save the updated file**.
     4. **Convert Excel to TSV**:
        - Use a Perl or Python script to convert the updated master table to a TSV (tab-separated values) file:
          ```bash
          perl sofa-excel2tsv.pl master_table.xlsx
          ```
          Or
          ```bash
          python sofa-excel2tsv.py master_table.xlsx
          ```
     5. **Compare old and new TSV files**:
        - Use any file comparison tool (e.g., `diff` in Unix) to ensure the new TSV file has the correct updates for the new site.
        - Resolve any discrepancies if found.
     6. **Rename the new TSV file**:
        - Rename the newly created TSV file to follow the naming convention:
          ```
          Adani.farm-static-data.current.tsv
          ```
     7. **Replace the old TSV file**:
        - Copy the newly created TSV file and replace the old one in the master table folder.
        - Example path: `d:\Anemos\config\sofa\master-table\`

---

## **2. TSDR (Time Series Data Repository) Configuration**
   - **Purpose**: Set up the TSDR to handle time series data for the new site.
   - **Steps**:
     1. **Run the TSDR context creation script**:
        - Use the following command to create the necessary context files for the new site:
          ```bash
          bash create-context.bash -s AGE25L -o AGE25L
          ```
     2. **Check the output**:
        - A folder named `AGE25L` will be created, containing XML files related to the context configuration.
     3. **Copy context files**:
        - Copy the generated XML files to the following location:
          ```
          d:\Anemos\temp\contexts\
          ```
     4. **Run the localhost script**:
        - Finalize the context setup by running:
          ```bash
          perl create-context.localhost
          ```
        - This will apply the new site’s context configuration to the system.

---

## **3. Update TSDR Configuration Files on Servers**
   - **Purpose**: Ensure TSDR configurations are applied across all servers.
   - **Steps**:
     1. **On Server 01**:
        - **Backup existing configuration**: Use Total Commander to zip the entire config folder (`Alt+F5`).
        - **Copy new context files**: Move the newly generated context files to:
          ```
          d:\Anemos\tmp\contexts\
          ```
        - **Run context creation script**:
          ```bash
          d:\Anemos\bin\scripts\create-contexts.localhost.bat
          ```
        - **Replace the repconfig.xml**: The `repconfig.xml` file in `d:\Anemos\config\tsdr\` needs to be updated with the new configuration for AGE25L.
     2. **On Server 02**:
        - **Copy repconfig.xml** from *Server 01* and place it in:
          ```
          d:\Anemos\config\tsdr\
          ```
        - **Restart Tomcat service**: 
          - Use Windows Services to restart the Tomcat service to apply the changes.
        - **Run TSDR test script**:
          ```bash
          d:\Anemos\bin\platform\clients\tsdr\tsdr-localhost-test.bat
          ```
        - Ensure that the test returns `RESCODE=0`, indicating that the TSDR is running correctly.

---

## **4. Prepare Application XML Files**
   - **Purpose**: Configure XML files required for importing data from external sources (e.g., NWP data).
   - **Steps**:
     1. **Run the Adani bash script**:
        - The following command will generate the necessary application XML files:
          ```bash
          bash call-Adani.bash
          ```
        - This script will call `create-app-xml.pl`, which uses the current TSV file and templates to generate XML files.
     2. **Check output**:
        - Navigate to the output folder where the new XML files are generated.
        - Review the log file for any warnings or errors.
     3. **Copy XML files**:
        - Copy the following files to their respective directories:
          - `Adani.ecmwf-grib-import-0012.xml`
          - `Adani.gfs-grib-import.xml`
          ```
          d:\Anemos\config\sdrxml\
          ```

---

## **5. Configure and Run Forecasting Models**
   - **Purpose**: Ensure the new site is integrated into the day-ahead and intraday forecasting systems.
   - **Steps**:
     1. **Backup current XML files**:
        - Copy files like `Adani.nwp-interpolation.xml` and `Adani.ecmwf_oshybrid-pv-py.xml` to a backup location (e.g., `d:\Anemos\oandm\cw\2024-09-17.AGE25L\`).
     2. **Edit forecasting XML files**:
        - Add the AGE25L site configuration to the following files:
          - `Adani.nwp-interpolation.xml`
          - `Adani.ecmwf_oshybrid-pv-py.xml`
          - `Adani.ncmrwf_oshybrid-pv-py.xml`
        - Add necessary site metadata (e.g., power curve, site coordinates).
     3. **Copy site configuration files**:
        - Copy the `AGE25L.siteconfig.json` file to the respective directories for different forecasting models:
          ```
          d:\Anemos\var\storage\ecmwf_oshybrid-pv-py\siteconfig\solar\
          d:\Anemos\var\storage\ncmrwf_oshybrid-pv-py\siteconfig\solar\
          ```
     4. **Re-run NWP models**:
        - Run the NWP interpolation model to ensure it includes the new site:
          ```bash
          /cygdrive/d/Anemos/bin/amwrapper/amwrapper.pl -L routine Adani nwp-interpolation 2024-09-18T00:00:00
          ```

---

## **6. Intraday Forecasting Models**
   - **Purpose**: Enable the intraday forecasting for the new site.
   - **Steps**:
     1. **Add new site to intraday files**:
        - Edit the following XML files to include AGE25L:
          - `Adani.osdyn-pv-py.xml`
          - `Adani.dynamic_postproc-solar-from-py.xml`
     2. **Copy site config files**:
        - Copy the `AGE25L.siteconfig.json` files to:
          ```
          d:\Anemos\var\storage\osdyn-pv-py\siteconfig\solar\
          ```
     3. **Re-run the intraday forecasting model**:
        - Run the operational model to check the intraday forecasts:
          ```bash
          /cygdrive/d/Anemos/bin/amwrapper/amwrapper.pl -L routine Adani osdyn-pv-py 2024-09-19T06:15:00
          ```

---

## **7. SCADA Data Import Configuration**
   - **Purpose**: Set up SCADA data import for the new site to enable real-time monitoring.
   - **Steps**:
     1. **Add new site to SCADA XML configuration**:
        - Insert the `ApplicationSolarFarm` element for AGE25L into `Adani.csv-meas-import-solar.xml`.
     2. **Modify SCADA parameters**:
        - Copy the `ApplicationParameters` from an existing site (e.g., Essel_150) and adjust according to AGE25L’s data.
     3. **Update preprocessing script**:
        - Edit the `preproc.rename-copy-scada-files-solar.pl` script to include the new site.
     4. **Check SCADA data import**:
        - Monitor the GUI for SCADA data imports to ensure it reflects the new site’s data.

---

## **8. Forecast Export Configuration**
   - **Purpose**: Export forecasts for the new site.
   - **Steps**:
     1. **Update export XML files**:
        - Add AGE25L to the following export files:
          - `Adani.wpp-export-solar-all.xml`
          - `Adani.wpp-export-solar-ctu.xml`
     2. **Verify export process**:
        - Check logs or the GUI to ensure the forecasts are exported correctly for the new site.

---

## **9. Update Static Plots and GUI**
   - **Purpose**: Display the new site in the graphical interface and plot

 generation tools.
   - **Steps**:
     1. **Add the site to static plot configuration files**:
        - Update the static plot XML files to include AGE25L:
          - `Adani.static-plots-dayahead.xml`
          - `Adani.static-plots-intraday.xml`
     2. **Update the GUI configuration**:
        - Edit the GUI configuration file to include AGE25L:
          ```
          Adani.anemosliveweb.xml
          ```
     3. **Restart Tomcat service**:
        - Restart Tomcat to apply the changes.
     4. **Verify the site in the GUI**:
        - Re-login and ensure the new site is visible in the GUI.

---

## **10. Final Verification and Testing**
   - **Purpose**: Ensure everything is configured correctly and running smoothly.
   - **Steps**:
     1. **Check SCADA imports and forecasts in the GUI**.
     2. **Verify that all configuration files have been updated correctly**.
     3. **Ensure that TSDR, forecasting models, and exports are working without errors**.
     4. **Run regression tests if available to confirm system stability**.

---
