def get_dns_severity():
    dns_severity = {
        0o1: "Informational",
        0o2: "Low",
        0o3: "Medium",
        0o4: "High",
        0o5: "Critical",
        0o6: "Severe",
        0o7: "Catastrophic"
    }

    octal_axis = {
        'yOct': [0o1, 0o2, 0o3, 0o4, 0o5, 0o6, 0o7],
        'xOct': [0o1, 0o2, 0o3, 0o4, 0o5, 0o6, 0o7]
    }

    combinations = []
    for y in octal_axis['yOct']:
        for x in octal_axis['xOct']:
            combinations.append({
                "y": dns_severity[y],
                "x": dns_severity[x],
                "product": oct(y * x)
            })

    return {
        "severity_levels": dns_severity,
        "octal_axis": octal_axis,
        "combinations": combinations
    }
