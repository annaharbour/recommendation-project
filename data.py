location = ['Dilworth', 'Ballantyne', 'South Park', 'Cherry', 'Belmont', 'Huntersville', 'Matthews', 'North Charlotte', 'Myers Park', 'NoDa', 'South End', 'Davidson', 'Fort Mill', 'Concord', 'University City', 'Providence', 'Center City', 'Plaza Midwood', 'Elizabeth', 'Eastover', 'Fourth Ward', 'Cotswold', 'Wesley Heights']
cafe_data = [
    # Dilworth
    ['Dilworth', "Dilworth Coffee", '3', '3', "22 Teutonic Ave."],
    ['Dilworth', "Not Just Coffee", '4', '4', "Atherton Mill, Charlotte, NC"],
    ['Dilworth', "Sunflour Baking Company", '5', '5', "Dilworth Crossing Shopping Center, Charlotte, NC"],
    ['Dilworth', "Undercurrent Coffee", '4', '5', "1500 South Blvd., Suite 101A, Charlotte, NC"],
    ['Dilworth', "Mugs Coffee", '5', '4', "5126 Park Road, Charlotte, NC"],

    # Ballantyne
    ['Ballantyne', "Rush Espresso Cafe", '5', '5', "14825 Ballantyne Village Way, Charlotte, NC"],
    ['Ballantyne', "Mugs Coffee", '4', '4', "210 E Trade St, Charlotte, NC"],
    ['Ballantyne', "Starbucks", '3', '3', "15105 John J Delaney Dr, Charlotte, NC"],
    ['Ballantyne', "The Flying Biscuit Cafe", '4', '4', "7930 Rea Rd, Charlotte, NC"],

    # South Park
    ['South Park', "Amélie's French Bakery", '5', '5', "4321 Park Rd, Charlotte, NC"],
    ['South Park', "Revolution Ale House Coffee", '4', '4', "4200 South Blvd, Charlotte, NC"],
    ['South Park', "The Suffolk Punch", '4', '5', "2911 Griffith St, Charlotte, NC"],
    ['South Park', "Starbucks", '3', '3', "4431 Barclay Downs Dr, Charlotte, NC"],

    # Cherry
    ['Cherry', "Central Coffee Co.", '5', '4', "1700 Camden Rd, Charlotte, NC"],
    ['Cherry', "Not Just Coffee", '4', '4', "2000 South Blvd, Charlotte, NC"],
    ['Cherry', "Sunflour Baking Company", '5', '5', "1404 East Blvd, Charlotte, NC"],
    ['Cherry', "Queen City Grounds", '4', '4', "644 N Church St, Charlotte, NC"],

    # Belmont
    ['Belmont', "Smelly Cat Coffeehouse", '5', '5', "514 East 36th St, Charlotte, NC"],
    ['Belmont', "Belmont Coffee Company", '4', '4', "24 S Main St, Belmont, NC"],
    ['Belmont', "Rita’s Coffee", '3', '3', "4250 Wilkinson Blvd, Belmont, NC"],
    ['Belmont', "Vintner's Coffee", '4', '5', "29 Catawba St, Belmont, NC"],
    ['Belmont', "River District Coffee", '5', '4', "500 Park St, Belmont, NC"],

    # Huntersville
    ['Huntersville', "The Coffee Cup", '5', '5', "10115 Gilead Rd, Huntersville, NC"],
    ['Huntersville', "Sweet Spoons", '4', '4', "10222 Northcross Dr, Huntersville, NC"],
    ['Huntersville', "Starbucks", '3', '3', "16425 Northcross Dr, Huntersville, NC"],

    # Matthews
    ['Matthews', "The Roasting Company", '5', '5', "144 Matthews Station St, Matthews, NC"],
    ['Matthews', "Café 24:4", '4', '4', "11525 Lyle Center Dr, Matthews, NC"],
    ['Matthews', "Noble Smoke", '5', '4', "9601 E Independence Blvd, Matthews, NC"],

    # North Charlotte
    ['North Charlotte', "Cup of Joe", '5', '5', "4820 Old Pineville Rd, Charlotte, NC"],
    ['North Charlotte', "Chai Pani", '4', '4', "1600 N Tryon St, Charlotte, NC"],
    ['North Charlotte', "Not Just Coffee", '5', '5', "2000 South Blvd, Charlotte, NC"],

    # Myers Park
    ['Myers Park', "Queen City Grounds", '5', '5', "644 N Church St, Charlotte, NC"],
    ['Myers Park', "Not Just Coffee", '4', '4', "2000 South Blvd, Charlotte, NC"],
    ['Myers Park', "The Greenhouse Coffee", '4', '4', "1500 E 6th St, Charlotte, NC"],

    # NoDa
    ['NoDa', "Smelly Cat Coffeehouse", '5', '5', "514 East 36th St, Charlotte, NC"],
    ['NoDa', "The Hobbyist", '4', '4', "2100 N Davidson St, Charlotte, NC"],
    ['NoDa', "Mac Tabby Cat Cafe", '3', '5', "516 E 15th St, Charlotte, NC"],
    ['NoDa', "Hex Coffee", '5', '5', "125 Remount Rd, Charlotte, NC"],

    # South End
    ['South End', "Not Just Coffee", '5', '5', "333 S Tryon St, Charlotte, NC"],
    ['South End', "South End Grind", '4', '4', "2101 South Blvd, Charlotte, NC"],
    ['South End', "Queen City Grounds", '5', '4', "644 N Church St, Charlotte, NC"],

    # Davidson
    ['Davidson', "Summit Coffee", '5', '5', "128 S Main St, Davidson, NC"],
    ['Davidson', "The Local Bean", '4', '4', "314 S Main St, Davidson, NC"],
    ['Davidson', "Cafe 100", '4', '5', "207 S Main St, Davidson, NC"],

    # Fort Mill
    ['Fort Mill', "The White Horse", '5', '5', "107 Main St, Fort Mill, SC"],
    ['Fort Mill', "Luna's Coffee", '4', '4', "2077 Main St, Fort Mill, SC"],
    ['Fort Mill', "Starbucks", '3', '3', "1000 Market St, Fort Mill, SC"],

    # Concord
    ['Concord', "The Roasted Bean", '5', '5', "2270 David McKee Dr, Concord, NC"],
    ['Concord', "One World Coffeehouse", '4', '4', "1915 S Union St, Concord, NC"],
    ['Concord', "The Coffee Shop", '4', '5', "14 Union St S, Concord, NC"],

    # University City
    ['University City', "Crema Espresso Bar", '5', '5', "8200 University City Blvd, Charlotte, NC"],
    ['University City', "Not Just Coffee", '4', '4', "2000 South Blvd, Charlotte, NC"],
    ['University City', "Starbucks", '3', '3', "9001 JM Keynes Dr, Charlotte, NC"],

    # Providence
    ['Providence', "Not Just Coffee", '5', '5', "1000 South Blvd, Charlotte, NC"],
    ['Providence', "Beans Coffee Bar", '4', '4', "8900 University City Blvd, Charlotte, NC"],

    # Center City
    ['Center City', "Coco and the Director", '5', '5', "100 W Trade St, Charlotte, NC"],
    ['Center City', "Not Just Coffee", '5', '5', "333 S Tryon St, Charlotte, NC"],
    ['Center City', "The Daily Press", '4', '5', "1427 South Blvd, Charlotte, NC"],

    # Plaza Midwood
    ['Plaza Midwood', "Undercurrent Coffee", '5', '5', "2012 Commonwealth Ave, Charlotte, NC"],
    ['Plaza Midwood', "Central Coffee Co.", '4', '4', "719 Louise Ave, Charlotte, NC"],
    ['Plaza Midwood', "Queen City Grounds", '5', '5', "644 N Church St, Charlotte, NC"],
    ['Plaza Midwood', "Waterbean Coffee", '4', '4', "616 North Tryon St, Charlotte, NC"],

    # Elizabeth
    ['Elizabeth', "The Little Spoon Cafe", '5', '5', "2519 N Davidson St, Charlotte, NC"],
    ['Elizabeth', "The Daily Press", '4', '4', "1427 South Blvd, Charlotte, NC"],

    # Eastover
    ['Eastover', "Not Just Coffee", '5', '5', "2000 South Blvd, Charlotte, NC"],
    ['Eastover', "Crave Coffee", '4', '4', "4115 Monroe Rd, Charlotte, NC"],

    # Fourth Ward
    ['Fourth Ward', "The Daily Press", '5', '5', "1427 South Blvd, Charlotte, NC"],
    ['Fourth Ward', "Mac Tabby Cat Cafe", '3', '5', "516 E 15th St, Charlotte, NC"],

    # Wesley Heights
    ['Wesley Heights', "The Daily Press", '5', '5', "1427 South Blvd, Charlotte, NC"],
    ['Wesley Heights', "Central Coffee Co.", '4', '4', "719 Louise Ave, Charlotte, NC"],
    ['Wesley Heights', "Smelly Cat Coffeehouse", '5', '5', "514 East 36th St, Charlotte, NC"],

    # Cotswold
    ['Cotswold', "Coffee & Crepes", '5', '5', "4263 Providence Rd, Charlotte, NC"],
    ['Cotswold', "The Flying Biscuit Cafe", '4', '5', "1001 S Tryon St, Charlotte, NC"],
    ['Cotswold', "Starbucks", '3', '3', "4320 Providence Rd, Charlotte, NC"],
    ['Cotswold', "Pulp Coffee", '5', '4', "5401 Old Pineville Rd, Charlotte, NC"],

    # Wesley Heights
    ['Wesley Heights', "The Daily Press", '5', '5', "1427 South Blvd, Charlotte, NC"],
    ['Wesley Heights', "Central Coffee Co.", '4', '4', "719 Louise Ave, Charlotte, NC"],
    ['Wesley Heights', "Smelly Cat Coffeehouse", '5', '5', "514 East 36th St, Charlotte, NC"],
]