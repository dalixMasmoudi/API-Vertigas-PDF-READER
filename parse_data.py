def parse_text(text: str) -> dict:
    lines = text.split('\n')
    structured_data = {}
    
    # Simple parsing logic for demonstration purposes
    for line in lines:
        if "Empfänger" in line:
            structured_data["recipient"] = line.split("Empfänger")[-1].strip()
        elif "Datum" in line:
            structured_data["date"] = line.split("Datum")[-1].strip()
        elif "DEV Buyer" in line:
            structured_data["buyer"] = "DEV Buyer"
        elif "Artikelbezeichnung" in line:
            structured_data["article"] = line.split("Artikelbezeichnung")[-1].strip()
        elif "Brutto" in line:
            structured_data["gross_weight"] = line.split("Brutto")[-1].strip()
        elif "Tara" in line:
            structured_data["tare_weight"] = line.split("Tara")[-1].strip()
        elif "Netto" in line:
            structured_data["net_weight"] = line.split("Netto")[-1].strip()
        ## ADD ANY MORE PARAMTERS YOU LIKE

    return structured_data