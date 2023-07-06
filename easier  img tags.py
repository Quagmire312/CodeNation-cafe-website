arr = ["3 chickens.jpg","background.jpg","cheese.jpg","chicken.jpg","chips.jpg","chocolate bars.jpg","croissant.jpg","espresso.jpg","hot choccie.jpg","latte.jpg","many chips.png","matcha latte.jpg","mocha.jpg","pain.jpg","quesedilla.jpg","redbull.jpg","tea.jpg","tuna.jpg"]

for i in range(len(arr)):
    print(f"""
<div class="picture">
<img class="fit" src="./pics/{arr[i]}"/>
</div>
""")
