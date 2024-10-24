import pandas as pd

# Load company data (expanded test data with more sectors)
def load_company_data():
    data = {
        "Company": [
            # Technology
            "Microsoft",
            "Apple",
            "Google",
            "IBM",
            "Oracle",
            "LinkedIn",
            "GitHub",
            "Xamarin",
            "Skype",
            "Minecraft",
            "Beats Electronics",
            "Shazam",
            "Siri Inc",
            "FileMaker",
            "Claris",
            "YouTube",
            "Android",
            "Nest",
            "Fitbit",
            "DeepMind",
            # Healthcare
            "Johnson & Johnson",
            "Pfizer",
            "UnitedHealth",
            "Merck",
            "Abbott",
            "Ethicon",
            "Janssen Biotech",
            "McNeil Consumer",
            "Actelion",
            "Biosense Webster",
            "Wyeth",
            "Hospira",
            "King Pharmaceuticals",
            "Medivation",
            "Anacor Pharmaceuticals",
            # Financials
            "JPMorgan Chase",
            "Bank of America",
            "Wells Fargo",
            "Citigroup",
            "Goldman Sachs",
            "Chase Bank",
            "Merrill Lynch",
            "U.S. Trust",
            "Wachovia",
            "First Union",
            # Consumer Discretionary
            "Amazon",
            "Tesla",
            "Home Depot",
            "Nike",
            "McDonald's",
            "Whole Foods",
            "Zappos",
            "Twitch",
            "Audible",
            "Ring",
            "SolarCity",
            "Maxwell Technologies",
            "Grohmann Engineering",
            "DeepScale",
            "Hibar Systems",
            # Communication Services
            "Facebook",
            "Netflix",
            "Disney",
            "Comcast",
            "AT&T",
            "Instagram",
            "WhatsApp",
            "Oculus VR",
            "CTRL-labs",
            "Giphy",
            "Pixar",
            "Marvel Entertainment",
            "Lucasfilm",
            "21st Century Fox",
            "Hulu",
            # Industrials
            "Boeing",
            "Caterpillar",
            "General Electric",
            "3M",
            "Honeywell",
            "Jeppesen",
            "Aviall",
            "Liquid Robotics",
            "Aurora Flight Sciences",
            "Insitu",
            # Consumer Staples
            "Procter & Gamble",
            "Coca-Cola",
            "PepsiCo",
            "Walmart",
            "Costco",
            "Gillette",
            "Duracell",
            "Braun",
            "Minute Maid",
            "Honest Tea",
            "Frito-Lay",
            "Quaker Oats",
            "Gatorade",
            "Tropicana",
            "SodaStream",
            # Energy
            "ExxonMobil",
            "Chevron",
            "Shell",
            "BP",
            "Total",
            "XTO Energy",
            "Mobil",
            "Unocal",
            "Atlantic Richfield",
            "Amoco",
            # Utilities
            "NextEra Energy",
            "Duke Energy",
            "Southern Company",
            "Dominion Energy",
            "Exelon",
            "Florida Power & Light",
            "Gulf Power",
            "Progress Energy",
            "Piedmont Natural Gas",
            "PECO Energy",
            # Real Estate
            "American Tower",
            "Prologis",
            "Crown Castle",
            "Equinix",
            "Public Storage",
            "CoreSite Realty",
            "Digital Realty Trust",
            "CyrusOne",
            "QTS Realty Trust",
            "Switch",
        ],
        "Parent": [
            # Technology
            "",
            "",
            "",
            "",
            "",
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Apple",
            "Apple",
            "Apple",
            "Apple",
            "Apple",
            "Google",
            "Google",
            "Google",
            "Google",
            "Google",
            # Healthcare
            "",
            "",
            "",
            "",
            "",
            "Johnson & Johnson",
            "Johnson & Johnson",
            "Johnson & Johnson",
            "Johnson & Johnson",
            "Johnson & Johnson",
            "Pfizer",
            "Pfizer",
            "Pfizer",
            "Pfizer",
            "Pfizer",
            # Financials
            "",
            "",
            "",
            "",
            "",
            "JPMorgan Chase",
            "Bank of America",
            "Bank of America",
            "Wells Fargo",
            "Wells Fargo",
            # Consumer Discretionary
            "",
            "",
            "",
            "",
            "",
            "Amazon",
            "Amazon",
            "Amazon",
            "Amazon",
            "Amazon",
            "Tesla",
            "Tesla",
            "Tesla",
            "Tesla",
            "Tesla",
            # Communication Services
            "",
            "",
            "",
            "",
            "",
            "Facebook",
            "Facebook",
            "Facebook",
            "Facebook",
            "Facebook",
            "Disney",
            "Disney",
            "Disney",
            "Disney",
            "Disney",
            # Industrials
            "",
            "",
            "",
            "",
            "",
            "Boeing",
            "Boeing",
            "Boeing",
            "Boeing",
            "Boeing",
            # Consumer Staples
            "",
            "",
            "",
            "",
            "",
            "Procter & Gamble",
            "Procter & Gamble",
            "Procter & Gamble",
            "Coca-Cola",
            "Coca-Cola",
            "PepsiCo",
            "PepsiCo",
            "PepsiCo",
            "PepsiCo",
            "PepsiCo",
            # Energy
            "",
            "",
            "",
            "",
            "",
            "ExxonMobil",
            "ExxonMobil",
            "Chevron",
            "BP",
            "BP",
            # Utilities
            "",
            "",
            "",
            "",
            "",
            "NextEra Energy",
            "NextEra Energy",
            "Duke Energy",
            "Duke Energy",
            "Exelon",
            # Real Estate
            "",
            "",
            "",
            "",
            "",
            "American Tower",
            "Equinix",
            "Equinix",
            "Equinix",
            "Equinix",
        ],
        "Industry": [
            # Technology
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            "Technology",
            # Healthcare
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            # Financials
            "Financials",
            "Financials",
            "Financials",
            "Financials",
            "Financials",
            "Financials",
            "Financials",
            "Financials",
            "Financials",
            "Financials",
            # Consumer Discretionary
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            "Consumer Discretionary",
            # Communication Services
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            "Communication Services",
            # Industrials
            "Industrials",
            "Industrials",
            "Industrials",
            "Industrials",
            "Industrials",
            "Industrials",
            "Industrials",
            "Industrials",
            "Industrials",
            "Industrials",
            # Consumer Staples
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            "Consumer Staples",
            # Energy
            "Energy",
            "Energy",
            "Energy",
            "Energy",
            "Energy",
            "Energy",
            "Energy",
            "Energy",
            "Energy",
            "Energy",
            # Utilities
            "Utilities",
            "Utilities",
            "Utilities",
            "Utilities",
            "Utilities",
            "Utilities",
            "Utilities",
            "Utilities",
            "Utilities",
            "Utilities",
            # Real Estate
            "Real Estate",
            "Real Estate",
            "Real Estate",
            "Real Estate",
            "Real Estate",
            "Real Estate",
            "Real Estate",
            "Real Estate",
            "Real Estate",
            "Real Estate",
        ],
        "Market Cap": [
            # Technology (in billions USD, approximated)
            1800,
            2100,
            1500,
            120,
            180,
            26,
            7.5,
            0.4,
            8.5,
            2.5,
            3,
            0.4,
            0.2,
            0.3,
            0.1,
            160,
            70,
            3.2,
            1.5,
            0.5,
            # Healthcare
            400,
            210,
            380,
            190,
            180,
            20,
            15,
            10,
            8,
            5,
            12,
            8,
            6,
            4,
            2,
            # Financials
            450,
            300,
            180,
            140,
            90,
            40,
            30,
            20,
            15,
            10,
            # Consumer Discretionary
            1600,
            600,
            330,
            170,
            160,
            13,
            1.2,
            3.8,
            0.3,
            1.2,
            5,
            0.2,
            0.1,
            0.05,
            0.02,
            # Communication Services
            800,
            230,
            320,
            210,
            200,
            100,
            19,
            2,
            0.5,
            0.4,
            13,
            10,
            4,
            71,
            15,
            # Industrials
            120,
            90,
            80,
            95,
            110,
            2,
            1.5,
            0.3,
            0.2,
            0.8,
            # Consumer Staples
            300,
            230,
            190,
            400,
            180,
            50,
            4.7,
            3,
            2,
            0.5,
            40,
            15,
            10,
            8,
            1,
            # Energy
            250,
            200,
            180,
            90,
            130,
            40,
            35,
            30,
            25,
            20,
            # Utilities
            90,
            65,
            60,
            55,
            40,
            15,
            5,
            10,
            8,
            6,
            # Real Estate
            110,
            70,
            65,
            60,
            40,
            5,
            4,
            3,
            2,
            1,
        ],
    }

    # Add CVS Health to the main company list if it's not already there
    if "CVS Health" not in data["Company"]:
        data["Company"].append("CVS Health")
        data["Parent"].append("")
        data["Industry"].append("Healthcare")
        data["Market Cap"].append(100)  # Approximate market cap

    # Add Teladoc Health to the main company list if it's not already there
    if "Teladoc Health" not in data["Company"]:
        data["Company"].append("Teladoc Health")
        data["Parent"].append("")
        data["Industry"].append("Healthcare")
        data["Market Cap"].append(4)  # Approximate market cap

    # Add Illumina to the main company list if it's not already there
    if "Illumina" not in data["Company"]:
        data["Company"].append("Illumina")
        data["Parent"].append("")
        data["Industry"].append("Healthcare")
        data["Market Cap"].append(30)  # Approximate market cap

    # Cross-sector acquisitions
    data["Company"].extend(
        [
            "Nuance Communications",
            "Aera Health",
            "Sentillion",  # Microsoft healthcare acquisitions
            "CloudMedx",
            "Canary Health",  # Microsoft healthcare acquisitions (fictional)
            "WeWork",
            "Regus",  # Microsoft real estate acquisitions (fictional)
            "Pillpack",
            "One Medical",
            "Zoox",  # Amazon healthcare and automotive acquisitions
            "MGM Studios",
            "Whole Foods Market",  # Amazon media and retail acquisitions
            "Fitbit",
            "Looker",
            "Mandiant",  # Google consumer electronics and cybersecurity acquisitions
            "Aetna",
            "Signify Health",  # CVS Health healthcare acquisitions
            "Livongo",
            "InTouch Health",  # Teladoc Health acquisitions
            "Grail",
            "Pacific Biosciences",  # Illumina acquisitions
        ]
    )
    data["Parent"].extend(
        [
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Microsoft",
            "Amazon",
            "Amazon",
            "Amazon",
            "Amazon",
            "Amazon",
            "Google",
            "Google",
            "Google",
            "CVS Health",
            "CVS Health",
            "Teladoc Health",
            "Teladoc Health",
            "Illumina",
            "Illumina",
        ]
    )
    data["Industry"].extend(
        [
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Real Estate",
            "Real Estate",
            "Healthcare",
            "Healthcare",
            "Automotive",
            "Media",
            "Consumer Staples",
            "Consumer Discretionary",
            "Technology",
            "Technology",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
            "Healthcare",
        ]
    )
    data["Market Cap"].extend(
        [
            16,
            0.5,
            0.2,
            0.3,
            0.1,
            5,
            3,
            0.75,
            3.9,
            1.2,
            8.5,
            13.7,
            2.1,
            2.6,
            5.4,
            69,
            8,
            18.5,
            1.9,
            7.1,
            1.1,
        ]
    )

    return pd.DataFrame(data)
