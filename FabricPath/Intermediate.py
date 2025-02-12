import streamlit as st

def app():
    # Title and Overview
    st.title("Learning Path 2: Fabric Application & Design (Intermediate Level)")
    st.markdown("""
    ### Goal:
    Develop skills in applying fabric properties to specific design scenarios and make informed choices for various types of projects.  
    **Duration**: 3-5 weeks  
    """)

    # Create tabs for each module
    tab1, tab2, tab3 = st.tabs(["Module 1: Advanced Fabric Types and Properties", 
                                "Module 2: Fabric Selection for Design Projects", 
                                "Module 3: Fabric Maintenance and Care"])

    # Module 1: Advanced Fabric Types and Properties
    with tab1:
        st.header("Module 1: Advanced Fabric Types and Properties")
        
        st.subheader("Lesson 1.1: Natural vs Synthetic Fibers")
        st.markdown("""
        - **Natural Fibers**:
            - **Wool**: 
                - Wool is a natural fiber obtained from the fleece of sheep. It's warm, elastic, and water-resistant.
                - **Pros**: 
                    - Wool is eco-friendly as it is biodegradable and renewable. 
                    - It’s naturally breathable and insulating, making it perfect for colder climates.
                    - Wool also absorbs moisture and wicks it away from the skin, keeping you dry and comfortable.
                - **Cons**:
                    - Wool tends to be more expensive than synthetic fibers.
                    - It's prone to shrinkage if washed improperly, and it can wrinkle more easily.
                    - Some people may find wool to be itchy or irritating to the skin.
            - **Linen**: 
                - Linen is derived from the flax plant and is known for its smooth, cool, and breathable qualities.
                - **Pros**: 
                    - Linen is highly breathable, making it ideal for warm climates.
                    - It’s eco-friendly, biodegradable, and requires fewer pesticides compared to cotton.
                    - Linen garments have a natural ability to wick moisture and are naturally antibacterial.
                - **Cons**:
                    - Linen is prone to wrinkles and requires careful ironing.
                    - It can be more expensive than other fibers.
                    - Linen garments may feel stiff and less soft compared to cotton or synthetic fabrics.

        - **Synthetic Fibers**:
            - **Polyester**:
                - Polyester is one of the most widely used synthetic fibers, created from petrochemical products.
                - **Pros**: 
                    - Polyester is durable, resistant to shrinkage, and wrinkle-resistant.
                    - It's affordable and can be easily dyed in a variety of colors.
                    - The fabric is versatile and is often used in a wide range of applications, from clothing to upholstery.
                - **Cons**: 
                    - Polyester is non-biodegradable, meaning it doesn't break down naturally in the environment.
                    - The fabric is less breathable than natural fibers like cotton and linen, which may cause discomfort in hot weather.
                    - Polyester can retain odors and may require more frequent washing.
            - **Spandex** (also known as Lycra or Elastane):
                - Spandex is a highly elastic synthetic fiber used for stretchable garments like activewear and swimwear.
                - **Pros**: 
                    - Spandex has a very high stretchability, making it ideal for garments that require flexibility.
                    - It’s durable, lightweight, and resistant to both water and oils.
                    - Spandex is breathable and retains its shape even after extensive wear.
                - **Cons**: 
                    - Like other synthetic fibers, Spandex is non-biodegradable.
                    - It’s often blended with other fibers to enhance elasticity, which can affect the overall durability and comfort of the garment.
                    - Spandex is sensitive to heat, which may cause it to degrade over time if exposed to high temperatures during washing or drying.

        - **Comparing Natural and Synthetic Fibers**:
            - **Cost**: Natural fibers tend to be more expensive due to their labor-intensive production methods and lower availability, while synthetic fibers are mass-produced and often more affordable.
            - **Sustainability**: Natural fibers are generally more eco-friendly, biodegradable, and renewable, making them a better choice for environmentally-conscious consumers. However, the cultivation of fibers like cotton and flax still requires water and land, which can lead to environmental concerns if not managed properly.
            - **Comfort and Durability**: Natural fibers are usually more comfortable to wear as they are breathable and soft, but synthetic fibers tend to be more durable and resistant to wear and tear. Synthetic fibers like polyester and spandex have also been engineered to enhance specific qualities like moisture-wicking, stretch, and shape retention.
            - **Environmental Impact**: Synthetic fibers contribute to pollution as they are made from petrochemical products and are non-biodegradable. However, natural fibers, though biodegradable, can still have a significant environmental footprint during their cultivation, particularly with regard to water usage and pesticide application.

        - **Choosing the Right Fiber**:
            - **For Hot Weather**: Linen, cotton, and certain blends are ideal for warm conditions due to their breathability and moisture-wicking properties.
            - **For Cold Weather**: Wool is an excellent choice due to its insulating properties and ability to retain heat.
            - **For Activewear**: Spandex and polyester are best suited for performance and stretch due to their elasticity and moisture-wicking abilities.
            - **For Everyday Clothing**: Polyester blends, which combine durability with comfort, are great for a wide variety of uses, from casual to semi-formal settings.
        """)

        st.subheader("Lesson 1.2: Blended Fabrics")
        st.markdown("""
        - **Why Blend Fabrics?**:  
            - Blending natural and synthetic fibers allows manufacturers to combine the best properties of both types of fibers. Natural fibers bring comfort, breathability, and eco-friendliness, while synthetic fibers add durability, elasticity, and wrinkle resistance.
            - **Goal of Blending**:  
            - Improve fabric performance: Combining different fibers helps to create fabrics that perform better under certain conditions (e.g., enhanced stretch, moisture-wicking, or durability).
            - Cost-effectiveness: Blended fabrics can provide a balance between high-quality natural fibers and affordable synthetic fibers, making them more affordable while maintaining good qualities.
            - Aesthetic appeal: Blends can also improve the appearance of fabrics, allowing manufacturers to create more versatile and stylish options.

        - **Common Fabric Blends**:
            - **Polyester-Cotton Blends**:
                - One of the most popular fabric blends, combining the softness and breathability of cotton with the durability and wrinkle-resistance of polyester.
                - **Uses**: T-shirts, casual wear, and bed linens.
                - **Pros**: These fabrics are often easy to care for, as they are less likely to wrinkle or shrink compared to pure cotton. They are durable and breathable, making them ideal for everyday wear.
                - **Cons**: These blends may still trap heat in hot conditions and can be less breathable than 100% cotton.
            
            - **Spandex-Cotton Blends**:
                - Spandex adds stretchability to cotton fabric, making the fabric more flexible and comfortable.
                - **Uses**: Activewear, leggings, and sportswear.
                - **Pros**: The blend of spandex and cotton allows for a snug fit that retains its shape. The cotton provides comfort, while the spandex offers enhanced movement and elasticity.
                - **Cons**: Spandex blends may lose their elasticity over time with repeated wear and washing.

            - **Polyester-Wool Blends**:
                - Blending polyester with wool enhances the durability of wool while maintaining its warmth and softness.
                - **Uses**: Suits, outerwear, and coats.
                - **Pros**: These blends are generally less expensive than 100% wool and more durable. They also resist wrinkles and are easier to care for than pure wool.
                - **Cons**: The polyester content may reduce some of the natural breathability of wool, making the fabric less comfortable in warmer conditions.

            - **Nylon-Polyester Blends**:
                - Combining nylon and polyester creates a fabric that is highly durable, resistant to wear and tear, and water-resistant.
                - **Uses**: Outdoor gear, jackets, and backpacks.
                - **Pros**: These blends are lightweight yet strong, providing excellent protection against the elements while remaining flexible and durable.
                - **Cons**: They may not be as breathable as natural fibers, which can be a disadvantage in hot weather.

            - **Silk-Cotton Blends**:
                - Blending silk with cotton creates a luxurious fabric with the softness and sheen of silk, balanced with the comfort and breathability of cotton.
                - **Uses**: High-end fashion, evening wear, and lingerie.
                - **Pros**: These fabrics have a smooth, soft feel and a refined appearance. They are lightweight and comfortable while offering a touch of luxury.
                - **Cons**: The fabric may not be as durable as other blends and could require more careful maintenance, such as dry cleaning.

        - **Advantages of Blended Fabrics**:
            - **Enhanced Performance**: Blending fibers allows the creation of fabrics with unique properties, such as increased stretch, moisture-wicking, and durability.
            - **Cost-Effective**: Blended fabrics can combine the best of both worlds, offering consumers affordable options that still provide the quality and functionality of more expensive materials.
            - **Improved Aesthetic Appeal**: Blends can be engineered to create fabrics with desirable visual and tactile qualities, such as softness, sheen, and color richness.
            
        - **Disadvantages of Blended Fabrics**:
            - **Maintenance**: Some blended fabrics may require special care instructions, such as dry cleaning, depending on the components in the blend.
            - **Reduced Natural Qualities**: In some blends, the properties of natural fibers may be diminished by the synthetic fibers, such as reduced breathability, moisture absorption, or softness.

        - **Choosing the Right Blend**:
            - **For Comfort**: If comfort is a priority, look for blends that include cotton, silk, or linen. These fabrics are breathable, soft, and ideal for everyday wear.
            - **For Durability**: Polyester and nylon blends are ideal for clothing that needs to withstand wear and tear, like outdoor gear and activewear.
            - **For Flexibility**: Spandex blends, especially with cotton or polyester, are perfect for activewear and sportswear due to their stretchability and ability to maintain shape.
            - **For Warmth**: Wool blends with polyester or nylon are great for colder weather, providing warmth while being more durable and easier to care for than 100% wool.
        """)
        # Quiz 1
        st.subheader("Quiz: Compare Natural, Synthetic, and Blended Fibers")
        question_1 = st.radio("1. Which is a benefit of natural fibers?", 
                            ["Durability", "Biodegradability", "Wrinkle-resistance", "Affordability"], key="q1_module1")
        question_2 = st.radio("2. Why are fabrics blended?", 
                            ["For style", "To lower costs", "To enhance properties", "For color options"], key="q2_module1")
        question_3 = st.radio("3. Which of the following is an example of a synthetic fiber?", 
                            ["Cotton", "Linen", "Polyester", "Wool"], key="q3_module1")
        question_4 = st.radio("4. What is a disadvantage of blended fabrics?", 
                            ["Increased durability", "Lower cost", "Potential reduced breathability", "Enhanced comfort"], key="q4_module1")
        question_5 = st.radio("5. Which blend is commonly used for activewear?", 
                            ["Silk-Cotton", "Polyester-Cotton", "Spandex-Cotton", "Polyester-Wool"], key="q5_module1")

        if st.button("Submit Quiz 1 Answers", key="quiz1"):
            score = 0
            if question_1 == "Biodegradability":
                score += 1
            if question_2 == "To enhance properties":
                score += 1
            if question_3 == "Polyester":
                score += 1
            if question_4 == "Potential reduced breathability":
                score += 1
            if question_5 == "Spandex-Cotton":
                score += 1
            st.success(f"You scored {score}/5 in this quiz!")

    # Module 2: Fabric Selection for Design Projects
    with tab2:
        st.header("Module 2: Fabric Selection for Design Projects")
        st.subheader("Lesson 2.1: Selecting Fabrics for Formal Wear")
        st.markdown("""
        - **Formal Wear Fabrics**:  
            - **Silk**:  
                - **Description**: Silk is a natural fiber known for its luxurious feel and smooth texture. It is highly sought after for its elegant drape and sheen, making it a top choice for high-end formal wear.  
                - **Common Uses**: Evening gowns, bridal dresses, luxurious blouses, and formal suits.  
                - **Benefits**: Silk is lightweight, breathable, and comfortable against the skin. It has an exquisite luster that creates a glowing effect under lighting, making it perfect for elegant evening events.  
                - **Considerations**: Silk can be expensive and delicate, requiring careful handling. It’s important to dry clean silk garments and avoid exposing them to direct sunlight, as it can fade the fabric.  
                
            - **Satin**:  
                - **Description**: Satin is a weave, not a fiber, typically made from silk, polyester, or acetate. It has a glossy, reflective surface that creates a smooth, shiny appearance, making it a popular choice for formal occasions.  
                - **Common Uses**: Formal dresses, evening gowns, prom dresses, bridesmaid dresses, and accessories such as sashes and bows.  
                - **Benefits**: Satin has a luxurious finish that adds a touch of glamour to any garment. Its smooth surface also gives the illusion of sleekness, flattering the body’s curves. It’s versatile and works well for both high-sheen evening wear and accessories like clutches.  
                - **Considerations**: Satin can be prone to wrinkling and may require special care when storing. If made from synthetic fibers, satin may not be as breathable as silk, so consider the season when choosing it.  
                
            - **Velvet**:  
                - **Description**: Velvet is a fabric with a rich, plush texture that gives it depth and warmth. It is made by weaving two layers of fabric together and then cutting one of the layers to create the velvet pile. It’s often used for formal wear due to its elegant, regal appearance.  
                - **Common Uses**: Formal dresses, evening gowns, special occasion dresses, and jackets. Velvet is also used for accessories like handbags, scarves, and shoes.  
                - **Benefits**: Velvet’s luxurious texture and depth make it ideal for formal occasions where the wearer wants to stand out. It is warm and perfect for winter events. The fabric’s rich colors, such as deep red, emerald green, and midnight blue, add to its opulent look.  
                - **Considerations**: Velvet can be difficult to care for, as it attracts dust and lint easily. It requires dry cleaning and should be stored away from direct light to avoid fabric degradation. Velvet may also feel heavy, so it's ideal for colder seasons.  
                
        - **Choosing the Right Fabric for Your Event**:  
            - **Consider the Season**:  
                - **Summer**: Opt for lightweight fabrics like silk or satin. These materials are breathable and perfect for warm weather events. Silk is especially ideal for hot climates as it keeps the wearer cool and comfortable.  
                - **Winter**: Velvet is a wonderful choice for winter events as it adds warmth and coziness. Its rich texture provides a perfect balance of elegance and practicality during colder months.  
                
            - **Event Type**:  
                - For **formal galas** or **evening balls**, silk and satin are often preferred due to their glossy finish and formal appeal.  
                - For **wedding dresses** or **bridal gowns**, silk and satin are popular choices for their refined and elegant appearance, while velvet is often used in colder climates or for winter weddings.  
                - **Consider the Drape**: A fabric's drape is how it falls and flows when worn. Silk and satin are known for their soft, fluid drape, which creates a beautiful silhouette. Velvet, on the other hand, has a heavier drape that is often used for structured or voluminous designs.  
                
        - **Fabric Care Tips**:  
            - **Silk**: Always dry clean silk garments to preserve their beauty and sheen. Avoid exposing silk to harsh sunlight for prolonged periods.  
            - **Satin**: Satin should be dry cleaned or gently hand washed, depending on the fabric content. Avoid hot water and tumble drying to prevent damaging the glossy finish.  
            - **Velvet**: Velvet requires delicate care. It’s best to dry clean velvet to maintain its plush texture. Avoid ironing velvet directly, as it can flatten the pile. Instead, steam it to remove wrinkles gently.
        """)

        st.subheader("Lesson 2.2: Selecting Fabrics for Casual and Everyday Wear")
        st.markdown("""
        - **Casual Wear Fabrics**:  
            - **Cotton**:  
                - **Description**: A natural fiber that is soft, lightweight, and breathable. Cotton is highly absorbent and comfortable, making it one of the most popular choices for casual wear.  
                - **Common Uses**: T-shirts, casual dresses, jeans, and undergarments.  
                - **Benefits**: Easy to care for, machine washable, and suitable for all seasons. Cotton allows for good airflow, keeping the wearer cool in warmer months.  
                - **Considerations**: Cotton can shrink after washing if not pre-treated. It also wrinkles easily and may not retain its shape as well as synthetic fabrics.  

            - **Denim**:  
                - **Description**: A durable and sturdy fabric made from cotton twill. Denim is iconic for its use in casual clothing and is often associated with jeans. It is available in various weights, allowing for year-round wear.  
                - **Common Uses**: Jeans, jackets, skirts, and overalls.  
                - **Benefits**: Extremely durable, resistant to wear and tear, and versatile. Denim ages well, often developing a unique patina with use, which adds to its character.  
                - **Considerations**: Denim can be heavy and less breathable compared to lighter fabrics like cotton. It also requires proper washing and drying techniques to prevent fading or shrinking.  

            - **Fleece**:  
                - **Description**: A synthetic fabric made from polyester, known for its soft, fluffy texture. Fleece is warm and comfortable, often used for casual and loungewear.  
                - **Common Uses**: Hoodies, jackets, sweatpants, blankets, and cold-weather accessories like scarves.  
                - **Benefits**: Lightweight yet warm, fleece wicks moisture away from the body, making it suitable for both casual wear and outdoor activities. It dries quickly and is low maintenance.  
                - **Considerations**: Fleece is less breathable than natural fibers and can retain odors if not washed properly. It’s also prone to pilling over time.  

        - **Choosing Fabrics for Everyday Wear**:  
            - **Seasonal Considerations**:  
                - **Summer**: Cotton and lightweight denim are ideal for hot weather due to their breathability and comfort.  
                - **Winter**: Fleece and thicker denim provide warmth and insulation, making them suitable for colder climates.  
            - **Lifestyle Factors**:  
                - For active lifestyles, fabrics like fleece or performance cotton blends work well due to their durability and ease of movement.  
                - For casual outings, lightweight cotton or stretch denim offers a balance of comfort and style.  

        - **Care Tips for Everyday Fabrics**:  
            - **Cotton**: Machine wash in warm or cold water and tumble dry on low heat. To prevent shrinkage, use pre-washed cotton or air dry when possible.  
            - **Denim**: Wash inside out in cold water to maintain color. Avoid frequent washing to preserve the fabric's integrity.  
            - **Fleece**: Wash in cold water and avoid using fabric softeners, which can damage the fibers. Air dry or tumble dry on low heat to prevent pilling.  
        """)

        st.subheader("Lesson 2.3: Fabrics for Outerwear and Utility")
        st.markdown("""
        - **Outerwear and Utility Fabrics**:  
            - **Tweed**:  
                - **Description**: Tweed is a woolen fabric known for its tightly woven structure and rough texture. It is traditionally associated with classic and sophisticated outerwear.  
                - **Common Uses**: Jackets, blazers, hats, and skirts.  
                - **Benefits**: Highly durable, insulating, and resistant to moisture and wear. Its structured appearance makes it a popular choice for tailored outerwear.  
                - **Considerations**: Tweed can be heavy and may require dry cleaning to maintain its quality.  

            - **Wool**:  
                - **Description**: A natural fiber obtained from sheep, wool is highly prized for its warmth and versatility. It comes in various types, such as merino wool, cashmere, and alpaca.  
                - **Common Uses**: Overcoats, peacoats, scarves, and gloves.  
                - **Benefits**: Excellent insulation, water-resistant to some extent, and naturally breathable. Wool retains warmth even when damp, making it ideal for cold and wet climates.  
                - **Considerations**: Wool garments often require hand washing or dry cleaning. It can be prone to pilling if not cared for properly.  

            - **Canvas**:  
                - **Description**: Canvas is a heavy-duty woven fabric, typically made from cotton or a cotton-polyester blend. It is renowned for its strength and durability.  
                - **Common Uses**: Backpacks, tote bags, outdoor gear, and workwear jackets.  
                - **Benefits**: Sturdy, abrasion-resistant, and relatively affordable. Canvas is also easy to waterproof, making it suitable for utility and outdoor applications.  
                - **Considerations**: Canvas can feel stiff initially and may require breaking in. It is not naturally water-resistant and often needs additional treatments for outdoor use.  

        - **Special Features of Outerwear Fabrics**:  
            - **Weather Resistance**: Many outerwear fabrics, such as tweed and wool, are designed to provide insulation and protection against wind and rain.  
            - **Durability**: Outerwear fabrics must withstand frequent use and exposure to harsh conditions. Canvas, for instance, is ideal for utility purposes due to its toughness.  
            - **Aesthetic Appeal**: Outerwear is not just functional; fabrics like tweed and wool add a stylish element to the garment.  

        - **Care Tips for Outerwear Fabrics**:  
            - **Tweed**: Spot clean when necessary and brush off dirt using a soft-bristled brush. Store in a cool, dry place to prevent moth damage.  
            - **Wool**: Hand wash with mild detergent or dry clean. Use garment bags to store wool coats and scarves to protect them from pests.  
            - **Canvas**: Clean with a damp cloth for minor stains or machine wash for deeper cleaning. Avoid using fabric softeners, as they can weaken the fibers.  

        - **Choosing the Right Outerwear Fabric**:  
            - **Cold Weather**: Wool and tweed provide excellent insulation and a polished appearance for professional or casual settings.  
            - **Outdoor Utility**: Canvas is ideal for rugged conditions, offering protection and durability for tasks like hiking or heavy-duty work.  
        """)


        # Quiz 2
        st.subheader("Quiz: Scenario-based Fabric Selection")

        question_3 = st.radio(
            "1. Which fabric is best for evening gowns?",
            ["Cotton", "Silk", "Denim", "Canvas"],
            key="q1_module2"
        )

        question_4 = st.radio(
            "2. What is the best fabric for jackets?",
            ["Velvet", "Tweed", "Fleece", "Linen"],
            key="q2_module2"
        )

        question_5 = st.radio(
            "3. Which fabric is the most durable for outdoor gear?",
            ["Silk", "Canvas", "Velvet", "Linen"],
            key="q3_module2"
        )

        question_6 = st.radio(
            "4. Which fabric would you choose for a summer dress?",
            ["Wool", "Linen", "Tweed", "Fleece"],
            key="q4_module2"
        )

        question_7 = st.radio(
            "5. What is the best method to care for a wool coat?",
            ["Machine wash hot", "Dry clean only", "Line dry in direct sunlight", "Iron on high heat"],
            key="q5_module2"
        )

        if st.button("Submit Quiz 2 Answers", key="quiz2"):
            score = 0
            if question_3 == "Silk":
                score += 1
            if question_4 == "Tweed":
                score += 1
            if question_5 == "Canvas":
                score += 1
            if question_6 == "Linen":
                score += 1
            if question_7 == "Dry clean only":
                score += 1
            
            st.success(f"You scored {score}/5 in this quiz!")

    with tab3:
    # Module 3: Fabric Maintenance and Care
        st.subheader("Lesson 3.1: Washing and Caring for Delicate Fabrics")
        st.markdown("""
        - **Delicate Fabrics**: Proper care ensures longevity and maintains the quality of delicate materials.
            - **Silk**:
                - Always hand wash in cold water to prevent shrinking or weakening of fibers.
                - Use a mild, pH-neutral detergent designed for delicate fabrics.
                - Avoid wringing or twisting silk; gently press out water and lay flat on a clean towel to air dry.
                - Never expose silk to direct sunlight during drying, as it may cause fading.
                - For stubborn stains or special garments, dry cleaning is recommended.
            - **Cashmere**:
                - Hand wash in lukewarm water with a gentle detergent or baby shampoo.
                - Avoid using fabric softeners, as they can coat the fibers and reduce softness.
                - Reshape the garment while damp and lay flat to dry to avoid stretching or distortion.
                - Fold cashmere garments instead of hanging them to prevent misshaping.
                - Dry cleaning is advised for heavily soiled or structured cashmere items.
            - **Velvet**:
                - Spot clean stains with a damp cloth or specialized velvet cleaner.
                - Avoid over-wetting the fabric, as this can damage the pile and leave water marks.
                - For large cleaning needs or persistent stains, always opt for professional dry cleaning.
                - Store velvet items on padded hangers to prevent creasing or crushing the fabric.
                - Avoid ironing velvet directly; use a steamer or place a cloth between the fabric and the iron on a low setting.

        - **General Tips for Delicates**:
            - Always check the care label before washing any garment.
            - Use mesh laundry bags if machine washing delicate fabrics is unavoidable.
            - Avoid high-spin cycles, hot water, or harsh detergents that can weaken fibers.
            - Store delicates in breathable fabric bags or drawers to protect them from dust and pests.
            - Handle garments with care when wet, as wet fibers are more fragile and prone to damage.
        """)


        st.subheader("Lesson 3.2: How to Extend the Life of Durable Fabrics")
        st.markdown("""
        - **Durable Fabrics**: Proper care ensures these fabrics maintain their resilience and usability over time.
            - **Wool**:
                - Use cold or lukewarm water to wash wool garments to prevent shrinking or felting.
                - Avoid high heat during drying; air drying is best. Lay the garment flat on a towel to maintain its shape.
                - Use a gentle detergent specifically designed for wool.
                - Avoid frequent washing; spot clean when possible to reduce wear.
                - Store wool garments in breathable garment bags to protect against moths.
            - **Polyester**:
                - Machine wash on a normal or gentle cycle with cold or warm water.
                - Avoid high heat during drying; use low heat settings or air dry to maintain the fabric's strength and shape.
                - Polyester is prone to static; use fabric softeners or dryer sheets during washing or drying.
                - Do not iron at high temperatures; use a low setting with a cloth between the iron and the fabric.

        - **Best Practices for Durable Fabrics**:
            - **Washing**:
                - Always separate laundry by color (e.g., lights, darks) and by fabric type (e.g., delicate vs durable).
                - Avoid overloading the washing machine to allow fabrics to move freely and get cleaned properly.
                - Turn garments inside out before washing to minimize fading and abrasion on the outer surface.
            - **Drying**:
                - Avoid prolonged exposure to direct sunlight, which can weaken fibers and fade colors.
                - Use low or no-heat drying options to protect fabric structure.
                - Shake out garments before drying to reduce wrinkles and improve drying efficiency.
            - **Storing**:
                - Store durable fabrics in a cool, dry place to prevent mold, mildew, or damage from pests.
                - Fold heavy items like wool sweaters to prevent stretching; hang lightweight polyester garments to maintain shape.
                - Use silica gel packets or moisture absorbers in storage areas to maintain a dry environment.
            - **General Maintenance**:
                - Repair minor damage (e.g., loose threads, small tears) promptly to prevent further wear.
                - Avoid exposing durable fabrics to harsh chemicals or abrasive surfaces.
                - Rotate usage of durable garments to distribute wear evenly and prolong their life.

        By following these care tips, you can maximize the lifespan and quality of your wool, polyester, and other durable fabrics.
        """)

        st.subheader("Quiz: Fabric Maintenance and Care")

        # MCQs for Module 3
        question_5 = st.radio(
            "1. How should you wash silk to avoid damage?", 
            ["Machine wash hot", "Hand wash with cold water", "Use fabric softener", "Dry clean only"], 
            key="q1_module3"
        )

        question_6 = st.radio(
            "2. What is the best way to dry wool after washing?", 
            ["Machine dry on high heat", "Air dry flat", "Hang in direct sunlight", "Line dry"], 
            key="q2_module3"
        )

        question_7 = st.radio(
            "3. What fabric care mistake can damage polyester?", 
            ["Ironing at low heat", "Drying at high heat", "Using fabric softener", "Hand washing"], 
            key="q3_module3"
        )

        question_8 = st.radio(
            "4. Why is it important to separate fabrics by type during washing?", 
            ["To save water", "To avoid mixing colors", "To prevent damage to delicate fabrics", "To reduce washing time"], 
            key="q4_module3"
        )

        question_9 = st.radio(
            "5. Which storage practice can damage wool garments?", 
            ["Folding sweaters", "Using breathable garment bags", "Exposing to direct sunlight", "Storing in cool, dry places"], 
            key="q5_module3"
        )

        # Quiz Submission
        if st.button("Submit Quiz 3 Answers", key="quiz3"):
            score = 0
            if question_5 == "Hand wash with cold water":
                score += 1
            if question_6 == "Air dry flat":
                score += 1
            if question_7 == "Drying at high heat":
                score += 1
            if question_8 == "To prevent damage to delicate fabrics":
                score += 1
            if question_9 == "Exposing to direct sunlight":
                score += 1

            # Display Quiz Results
            st.success(f"You scored {score}/5 in this quiz!")
            if score == 5:
                st.header("Next Steps")
                st.markdown("""
                Congratulations on completing the **Intermediate Learning Path**!  
                - **Next Steps**: Proceed to the **Advanced Learning Path** for in-depth expertise in fabric design and application.  
                - **Keep Practicing**: Use the Fabric Explorer tool to experiment with different fabric scenarios.  

                Happy Learning!  
                """)
            elif score >= 3:
                st.markdown(f"""
                    Great job! You scored {score}/5. Review the lessons for even better results and proceed to the **Advanced Learning Path**.  
                """)
            elif score == 2:
                st.markdown("""
                    You scored 2/5. Brush up on your fabric care knowledge and try again!  
                """)
            else:
                st.error("You scored less than 2/5. Revisit the fabric care lessons and retake the quiz!")


# Run as a standalone app
if __name__ == "__main__":
    app()
