lines = [
    "Trees are essential to life on Earth.",
    "Trees release oxygen that people and animals need.",
    "Trees absorb carbon dioxide and help the air stay cleaner.",
    "Trees hold soil in place and reduce erosion.",
    "Trees provide shelter for birds, insects, and mammals.",
    "Trees create shade that makes summer days more comfortable.",
    "Trees make parks, streets, and homes more beautiful.",
    "Trees help cool cities and reduce heat in neighborhoods.",
    "Trees support pollinators with nectar, pollen, and habitat.",
    "Trees produce fruits, nuts, seeds, and wood for life.",
    "Trees grow from tiny seeds into strong living giants.",
    "Trees have roots, trunks, branches, and leaves that work together.",
    "Trees use sunlight to make food through photosynthesis.",
    "Trees store energy in their trunks and roots.",
    "Trees can live for many years and become part of history.",
    "Trees improve mood and help people feel calmer and happier.",
    "Trees filter dust and make the air feel fresher.",
    "Trees can reduce noise and make busy places quieter.",
    "Trees protect crops from wind and harsh weather.",
    "Trees help forests stay healthy and full of life.",
    "Trees are home to many creatures, from birds to fungi.",
    "Trees can grow in deserts, mountains, wetlands, and valleys.",
    "Trees differ by species, size, color, and leaf shape.",
    "Trees can be evergreen, deciduous, tropical, or alpine.",
    "Trees provide natural beauty in every season of the year.",
    "Trees in spring grow fresh buds and bright green leaves.",
    "Trees in summer spread wide canopies of shade.",
    "Trees in autumn glow with red, orange, and gold.",
    "Trees in winter reveal graceful branches against the sky.",
    "Trees have bark that protects them from insects and weather.",
    "Trees carry water from the ground up through their trunks.",
    "Trees can be planted to restore damaged land.",
    "Trees help slow rainwater runoff and reduce flooding.",
    "Trees support the water cycle with leaves and roots.",
    "Trees give us wood for homes, furniture, and tools.",
    "Trees provide paper, rubber, medicine, and many useful materials.",
    "Trees are important for biodiversity and natural balance.",
    "Trees can live longer than many generations of people.",
    "Trees are symbols of strength, patience, and hope.",
    "Trees remind us that steady growth takes time.",
    "Trees often become landmarks in gardens, parks, and forests.",
    "Trees are loved by children who climb and explore them.",
    "Trees make forests feel deep, quiet, and magical.",
    "Trees are a gift to the Earth and to every living thing.",
    "Trees can grow from seeds, nuts, or cuttings in the soil.",
    "Trees feed the soil when leaves fall and decay.",
    "Trees create homes for insects that feed birds and animals.",
    "Trees can protect roads, farms, and homes from wind damage.",
    "Trees help keep ecosystems connected and healthy.",
    "Trees strengthen the soil and hold the ground together.",
    "Trees are often planted to celebrate life and new beginnings.",
    "Trees can be tall, short, wide, twisted, or graceful.",
    "Trees are part of the natural story of the planet.",
    "Trees help keep the climate more stable over time.",
    "Trees can reduce the effects of heatwaves in cities.",
    "Trees make the world feel greener, calmer, and kinder.",
    "Trees hold water in the soil and support nearby plants.",
    "Trees make wonderful places for rest, reflection, and joy.",
    "Trees provide oxygen for every breath we take.",
    "Trees are essential for healthy ecosystems and clean air.",
    "Trees feed the earth and shelter the creatures around them.",
    "Trees can be found in forests, gardens, farms, and wild lands.",
    "Trees are admired for their beauty, strength, and age.",
    "Trees make the landscape rich with color and movement.",
    "Trees support fungi, mosses, and tiny living organisms.",
    "Trees grow slowly but leave lasting beauty for everyone.",
    "Trees are valuable for both nature and human life.",
    "Trees can grow in cold places as well as warm ones.",
    "Trees become homes for nests, holes, and hidden shelters.",
    "Trees absorb sound and help make places more peaceful.",
    "Trees help shape the world through every season.",
    "Trees are full of life from roots to crown.",
    "Trees bring color to the sky and freshness to the air.",
    "Trees inspire artists, poets, and dreamers everywhere.",
    "Trees protect the soil and keep rivers cleaner.",
    "Trees are reminders that life grows with patience.",
    "Trees stand tall and quietly support the natural world.",
    "Trees are one of Earth’s most important living treasures.",
    "Trees deserve care, respect, and protection from everyone.",
]

if len(lines) != 100:
    raise SystemExit(f'Expected 100 lines, got {len(lines)}')

html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>allign</title>
    <link rel=\"stylesheet\" href=\"style1.css\">
</head>
<body>
    <img src=\"https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg\" alt=\"\">
    <pre>""" + "\n".join(lines) + "</pre>\n</body>\n</html>"

with open('alligning.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Wrote', len(lines), 'lines to alligning.html')
