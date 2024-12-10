# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 00:29:06 2024

@author: Franz Guzman
"""

import rtds.rscadfx
import time

# Open a connection to RSCAD FX from the script.
# Any code executed within the following block will run while connected to RSCAD FX.
with rtds.rscadfx.remote_connection() as app:

    # Open the case file
    case_id1 = app.open_case(r"C:\Users\Franz Guzman\OneDrive\2. TRABAJO - RODRIGO\Archivos - Auxiliares\Documents\RSCAD\RTDS_USER_FX\fileman\6. Sexta_Aula\Teste_2_Python.rtfx")
    Teste_2_Python = case_id1.draft.get_subpage("SS #1")

    # Create a Source component
    lf_rtds_sharc_sld_SRC_id = Teste_2_Python.insert_component("lf_rtds_sharc_sld_SRC", 176, 112)  # Specify coordinates
    SRC_id = lf_rtds_sharc_sld_SRC_id.unique_id  # Get the unique ID of the component
 
    # Set parameters for the Source component
    lf_rtds_sharc_sld_SRC_id = case_id1.get_object(SRC_id)  # Retrieve the component by ID
    lf_rtds_sharc_sld_SRC_id.set_parameter("Name", "SRC_001")  # Set the source name
    lf_rtds_sharc_sld_SRC_id.set_parameter("ZSeq", "Yes")  # Enable zero-sequence impedance
    lf_rtds_sharc_sld_SRC_id.set_parameter("ZType", "R-L")  # Set zero-sequence type to R-L
    lf_rtds_sharc_sld_SRC_id.set_parameter("R1s", "2.0")  # Set series resistance (Ohms)
    lf_rtds_sharc_sld_SRC_id.set_parameter("R1p", "1.0e6")  # Set parallel resistance (Ohms)
    lf_rtds_sharc_sld_SRC_id.set_parameter("L1p", "2.0")  # Set inductance (Henries)
    lf_rtds_sharc_sld_SRC_id.set_parameter("R0p", "2.0")  # Set zero-sequence resistance (Ohms)
    lf_rtds_sharc_sld_SRC_id.set_parameter("L0p", "1.0")  # Set zero-sequence inductance (Henries)
    lf_rtds_sharc_sld_SRC_id.set_parameter("Es", "400.0")  # Set source voltage (kV)
    lf_rtds_sharc_sld_SRC_id.set_parameter("F0", "50.0")  # Set source frequency (Hz)
    lf_rtds_sharc_sld_SRC_id.set_parameter("Ph", "5.0")  # Set phase angle (Degrees)
    # Enable current monitoring
    lf_rtds_sharc_sld_SRC_id.set_parameter("Imon", "Yes")  # Enable current monitoring
    lf_rtds_sharc_sld_SRC_id.set_parameter("IAnam", "IA_001")  # Assign name for phase A current
    lf_rtds_sharc_sld_SRC_id.set_parameter("IBnam", "IB_001")  # Assign name for phase B current
    lf_rtds_sharc_sld_SRC_id.set_parameter("ICnam", "IC_001")  # Assign name for phase C current
    # Enable the breaker
    lf_rtds_sharc_sld_SRC_id.set_parameter("srcBrk", "Yes")  # Enable the breaker
    lf_rtds_sharc_sld_SRC_id.set_parameter("swdnm", "S_BK_001")  # Assign name for the breaker
    # Enable power monitoring
    lf_rtds_sharc_sld_SRC_id.set_parameter("Pmon", "Yes")  # Enable active power monitoring
    lf_rtds_sharc_sld_SRC_id.set_parameter("Qmon", "Yes")  # Enable reactive power monitoring
    lf_rtds_sharc_sld_SRC_id.set_parameter("Pnam", "P_001")  # Set name for active power
    lf_rtds_sharc_sld_SRC_id.set_parameter("Qnam", "Q_001")  # Set name for reactive power
    
    # Create an empty list for storing configuration data
    data = []
    
    # Append configuration data for the Source component
    data.append({
        "ID": SRC_id,
        "Name": "SRC_001",
        "ZSeq": "Yes",
        "ZType": "R-L",
        "Es": "400.0",
        "Ph": "5.0",
        "Imon": "Yes",
        "srcBrk": "Yes",
        "swdnm": "S_BK_001",
        "Pmon": "Yes",
        "Qmon": "Yes",
        "Pnam": "P_001",
        "Qnam": "Q_001"
    })

    # Display the configuration table
    print("\nConfiguration Table:")
    print(f"{'ID':<5}{'Name':<10}{'ZSeq':<10}{'ZType':<10}{'Es':<10}{'Ph':<10}{'Imon':<10}{'srcBrk':<10}{'swdnm':<10}{'Pmon':<10}{'Qmon':<10}{'Pnam':<10}{'Qnam':<10}")
    for row in data:
        print(f"{row['ID']:<5}{row['Name']:<10}{row['ZSeq']:<10}{row['ZType']:<10}{row['Es']:<10}{row['Ph']:<10}{row['Imon']:<10}{row['srcBrk']:<10}{row['swdnm']:<10}{row['Pmon']:<10}{row['Qmon']:<10}{row['Pnam']:<10}{row['Qnam']:<10}")
