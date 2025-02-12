import streamlit as st

def app():
    # Title and Overview
    st.title("Learning Path 1: Fabric Basics (Beginner Level)")
    st.markdown("""
    ### Goal:
    Introduce students to fabric types, basic properties, and initial fabric selection knowledge.
    """)

    # Create tabs for each module
    tab1, tab2, tab3 = st.tabs(["Module 1: Introduction to Fabrics", 
                                "Module 2: Fabric Properties", 
                                "Module 3: Basic Uses of Fabrics"])
    with tab1:
        # Module 1 Title
        st.header("Module 1: Introduction to Fabrics")
        
        # Lesson 1.1: What are Fabrics?
        st.subheader("Lesson 1.1: What are Fabrics?")
        st.markdown("""
        ### Overview of Fabric Fibers
        Fabrics are materials made from fibers, which are spun into threads and then woven, knitted, or bonded to create textiles. They can be classified into four main categories:

        1. **Natural Fibers**:  
        - Derived from plants or animals.  
        - **Examples**:  
            - *Plant-based*: Cotton, Linen (from flax).  
            - *Animal-based*: Wool (sheep), Silk (silkworm), Alpaca, Cashmere (goat).  
        - **Key Features**: Breathable, biodegradable, and often soft to touch.  

        2. **Synthetic Fibers**:  
        - Man-made fibers created from petrochemicals.  
        - **Examples**: Polyester, Nylon, Acrylic, Spandex.  
        - **Key Features**: Durable, elastic, resistant to wrinkles, but less breathable.  

        3. **Semi-Synthetic Fibers**:  
        - Made by chemically treating natural materials (like cellulose from wood pulp).  
        - **Examples**: Rayon, Modal, Lyocell.  
        - **Key Features**: Soft, absorbent, drapes well, and eco-friendlier than fully synthetic fibers.  

        4. **Blended Fibers**:  
        - Combination of two or more fiber types to enhance functionality.  
        - **Examples**: Poly-cotton (polyester + cotton), Wool-acrylic.  
        - **Key Features**: Balance of natural and synthetic properties, such as breathability and durability.
        """)

        st.markdown("""
        #### Basic Fiber Classification
        - **Plant-Based Fibers**: Focused on cellulose (e.g., Cotton, Linen). These are breathable and often absorb moisture well.  
        - **Animal-Based Fibers**: Based on protein (e.g., Wool, Silk). Known for warmth and luxury.  
        - **Synthetic Fibers**: Derived from petrochemicals (e.g., Polyester, Nylon). Engineered for strength and resistance.  
        - **Blends**: Hybrid fibers that combine the best qualities of their components.  
        """)

        # Lesson 1.2: How Fabrics are Made
        st.subheader("Lesson 1.2: How Fabrics are Made")
        st.markdown("""
        #### Processes
        1. **Spinning**:  
        - Fibers are drawn out and twisted together to create yarn.  
        - Methods: Hand spinning, mechanical spinning (modern machines).  
        - Example: Turning cotton fibers into threads.  

        2. **Weaving**:  
        - Interlacing two sets of yarn (warp and weft) at right angles to create a fabric.  
        - Patterns: Plain weave, twill weave, satin weave.  
        - Common Fabrics: Denim (twill weave), Satin (satin weave).  

        3. **Knitting**:  
        - Creating fabric by looping threads together in rows or patterns.  
        - Types: Hand knitting, machine knitting.  
        - Common Fabrics: Jersey, Rib-knit (used in T-shirts, sweaters).  

        4. **Non-woven Methods**:  
        - Fibers are bonded together using heat, pressure, or adhesives instead of weaving/knitting.  
        - Common in disposable products like surgical masks or felt.  
        """)

        st.markdown("""
        #### Finishes and Treatments
        - **Purpose**: Enhance fabric functionality and durability.  
        - **Examples**:  
        1. **Stain Resistance**: Treated with special coatings to repel liquids (e.g., Scotchgard-treated upholstery).  
        2. **Waterproofing**: Adding layers or sprays to make fabric water-resistant (e.g., Gore-Tex jackets).  
        3. **Fire Retardant**: Fabrics treated to reduce flammability (e.g., for curtains and uniforms).  
        4. **Softening or Texturing**: To improve comfort or appearance.  
        5. **Anti-Wrinkle**: For easy maintenance (e.g., wrinkle-free shirts).  
        """)

        # Quiz 1
        st.subheader("Quiz: Fabric Classification and Production")
        question_1 = st.radio(
            "1. Which of the following is an example of a semi-synthetic fiber?",
            ["Cotton", "Rayon", "Polyester", "Wool"], 
            key="q1_module1"
        )

        question_2 = st.radio(
            "2. What process involves twisting fibers together to form yarn?",
            ["Knitting", "Spinning", "Weaving", "Bonding"], 
            key="q2_module1"
        )

        question_3 = st.radio(
            "3. What is the main difference between natural and synthetic fibers?",
            ["Cost", "Source of origin", "Durability", "Availability"], 
            key="q3_module1"
        )

        question_4 = st.radio(
            "4. What type of weave pattern is most commonly used in denim fabrics?",
            ["Plain weave", "Twill weave", "Satin weave", "Rib-knit"], 
            key="q4_module1"
        )

        question_5 = st.radio(
            "5. Which finish would you apply to fabric for waterproofing?",
            ["Fire retardant", "Softening", "Scotchgard treatment", "Anti-wrinkle"], 
            key="q5_module1"
        )

        if st.button("Submit Quiz 1 Answers", key="quiz1"):
            score = 0
            if question_1 == "Rayon":
                score += 1
            if question_2 == "Spinning":
                score += 1
            if question_3 == "Source of origin":
                score += 1
            if question_4 == "Twill weave":
                score += 1
            if question_5 == "Scotchgard treatment":
                score += 1
            
            st.success(f"You scored {score}/5 in this quiz!")


    # Module 2: Fabric Properties
    with tab2:
        st.header("Module 2: Fabric Properties")
        
        st.subheader("Lesson 2.1: Durability of Fabrics")
        st.markdown("""
        - **Fabric Durability**:  
        - Durability refers to how well a fabric resists wear and tear, fading, and damage over time.
        - **High Durability Fabrics**:  
            - **Polyester**: Known for its resilience, polyester is durable, resistant to shrinking, and holds its color well.
            - **Wool**: While natural, wool is highly durable, resilient to wrinkles, and has insulating properties.
        - **Low Durability Fabrics**:  
            - **Silk**: A delicate, luxury fabric that requires special care. It is prone to snags and fading with prolonged exposure to light.
            - **Linen**: Though strong, linen wrinkles easily and is less durable compared to synthetic fibers.
        - **Care for Durability**:  
        - **Polyester**: Machine washable, can withstand high heat in dryers.  
        - **Wool**: Hand wash in cold water or dry clean to preserve its structure.
        - **Silk and Linen**: Hand wash with mild detergent and avoid high heat to maintain their lifespan.

        """)
        
        st.subheader("Lesson 2.2: Fabric Texture and Appearance")
        st.markdown("""
        - **Smooth Fabrics**:  
        - **Silk**: Soft, smooth, and lustrous with a high sheen. Ideal for formal wear and luxury garments.
        - **Satin**: A smooth fabric with a glossy surface, often used in evening gowns and wedding dresses.
        - **Rough Fabrics**:  
        - **Wool**: Typically thicker and coarser in texture, giving it warmth and a rich, textured appearance.
        - **Linen**: Has a natural roughness, which contributes to its rustic, casual look. It wrinkles easily, which is part of its charm.
        - **Other Textured Fabrics**:  
        - **Velvet**: Known for its soft, plush texture, velvet is often used for luxury home decor and clothing.
        - **Cotton**: While smoother than wool or linen, cotton has a medium texture that can vary depending on weave (e.g., soft in T-shirts, rougher in canvas).

        """)
        
        # Quiz 2
        st.subheader("Quiz: Fabric Durability and Texture Matching")
        question_1 = st.radio("1. Which of the following fabrics is highly durable?", 
                            ["Silk", "Wool", "Linen", "Velvet"], key="q1_module2")
        question_2 = st.radio("2. Which fabric has a smooth texture?", 
                            ["Wool", "Silk", "Denim", "Linen"], key="q2_module2")
        question_3 = st.radio("3. Which fabric is most resistant to wear and tear?", 
                            ["Silk", "Polyester", "Cotton", "Linen"], key="q3_module2")
        question_4 = st.radio("4. What fabric is known for a rough texture?", 
                            ["Silk", "Wool", "Denim", "Satin"], key="q4_module2")
        question_5 = st.radio("5. Which fabric is ideal for formal wear due to its smooth and glossy finish?", 
                            ["Wool", "Linen", "Satin", "Velvet"], key="q5_module2")
        
        if st.button("Submit Quiz 2 Answers", key="quiz2"):
            score = 0
            if question_1 == "Wool":
                score += 1
            if question_2 == "Silk":
                score += 1
            if question_3 == "Polyester":
                score += 1
            if question_4 == "Wool":
                score += 1
            if question_5 == "Satin":
                score += 1
            st.success(f"You scored {score}/5 in this quiz!")

    # Module 3: Basic Uses of Fabrics
    with tab3:
        st.header("Module 3: Basic Uses of Fabrics")
        
        # Lesson 3.1: Common Fabric Uses# Lesson 3.1: Common Fabric Uses
        st.subheader("Lesson 3.1: Common Fabric Uses")
        st.markdown("""
        - **Everyday Fabrics**:
            - **Cotton**: 
                - Widely used for casual wear, such as t-shirts, jeans, casual dresses, and pajamas.
                - Cotton is breathable, lightweight, and easy to care for. It's also hypoallergenic, making it a great choice for sensitive skin.
                - **Common Uses**: T-shirts, denim jeans, casual shirts, baby clothes, bedsheets.
            - **Linen**:
                - Linen is a lightweight fabric ideal for summer wear, such as dresses, shirts, and pants. It’s cool, breathable, and has a slightly textured feel.
                - Known for its moisture-wicking properties, linen is perfect for hot climates and humid weather.
                - **Common Uses**: Summer dresses, linen shirts, beachwear, tablecloths, and curtains.
            - **Polyester**:
                - Known for its versatility, durability, and low-maintenance care. It's used for everyday garments like workwear, jackets, activewear, and outerwear.
                - Polyester resists wrinkles, is resistant to shrinking, and retains its shape well, making it a great option for clothing that requires little upkeep.
                - **Common Uses**: Jackets, sportswear, upholstery, home furnishings, and corporate uniforms.

        - **Choosing the Right Fabric**:
            - **Casual Settings**:
                - For everyday comfort and easy maintenance, fabrics like **cotton**, **denim**, and **polyester** are ideal. These fabrics are durable, breathable, and generally machine washable.
                - **Cotton** is a go-to fabric for relaxed styles such as casual t-shirts and hoodies, while **polyester** is often used in athletic and outdoor wear due to its durability and quick-drying properties.
            - **Formal Settings**:
                - Fabrics like **wool**, **silk**, and **linen** are typically chosen for more polished, sophisticated outfits such as suits, dresses, and office wear.
                - **Wool** is often used in formal attire like suits and coats because of its elegant drape and insulation properties.
                - **Silk** is a luxurious fabric perfect for high-end evening wear, blouses, and delicate lingerie. It’s known for its shiny, smooth texture and comfort.
                - **Linen** is popular for business casual attire, especially in the warmer months, because of its lightness and breathable properties.

        - **Specialized Fabrics**:
            - **Leather**:
                - Leather is a durable and rugged fabric commonly used in jackets, pants, shoes, and accessories like bags and belts. It provides warmth and protection against the elements.
                - **Common Uses**: Leather jackets, handbags, shoes, upholstery.
            - **Denim**:
                - A versatile fabric known for its durability, denim is used in a variety of settings, from casual to semi-formal. It’s commonly used in jeans, jackets, and skirts.
                - **Common Uses**: Jeans, jackets, skirts, shirts, bags.

        - **Eco-Friendly Fabrics**:
            - **Hemp**:
                - Hemp fabric is a sustainable, eco-friendly option made from the hemp plant. It is known for its durability and breathability, often used for eco-conscious clothing and accessories.
                - **Common Uses**: Casual wear, eco-friendly bags, sustainable shoes, and bedding.
            - **Recycled Polyester**:
                - Recycled polyester is made from post-consumer plastic bottles, offering a sustainable alternative to traditional polyester while maintaining the fabric's strength and durability.
                - **Common Uses**: Activewear, jackets, and bags.

        - **Weather-Specific Fabrics**:
            - **Water-Resistant Fabrics**:
                - Fabrics like **nylon** and **polyester** are often treated to be water-resistant, making them ideal for outdoor wear, rain jackets, and activewear.
                - **Common Uses**: Rain jackets, umbrellas, outdoor gear, and sportswear.
            - **Thermal Fabrics**:
                - Fabrics like **fleece** and **wool** are designed to trap warmth, making them perfect for cold-weather clothing.
                - **Common Uses**: Sweaters, thermal wear, winter coats, and scarves.
        """)
        # Lesson 3.2: Fabric Care and Maintenance
        st.subheader("Lesson 3.2: Fabric Care and Maintenance")
        st.markdown("""
        - **Washing and Drying Instructions**:
            - **Cotton**: 
                - Cotton is typically machine washable in warm water, but it should be washed separately to avoid color bleeding.
                - Tumble dry on low heat to avoid shrinkage, though air drying is preferred to keep the fabric in the best condition.
                - **Tip**: Use a mild detergent to preserve color and fabric integrity.
            - **Linen**: 
                - Linen should be hand washed or machine washed on a gentle cycle in cold water to prevent damage and reduce shrinkage.
                - It is best to line dry linen fabric. Avoid using the tumble dryer to keep the fabric from becoming stiff.
                - **Tip**: Iron linen while it's still slightly damp to prevent wrinkles.
            - **Polyester**: 
                - Polyester is easy to care for and can be machine washed on a gentle cycle in warm or cold water.
                - It can be air dried or tumble dried on low heat to maintain the fabric’s shape and durability.
                - **Tip**: Avoid high heat, which may cause the fabric to lose its shape.
            - **Silk**: 
                - Silk should be hand washed in cold water using a gentle detergent or dry cleaned, as it is a delicate fabric.
                - Never wring or twist silk to avoid damaging the fibers.
                - **Tip**: Use a mesh laundry bag if machine washing is necessary, and always wash with similar colors.

        - **Storing Fabrics**:
            - **General Storage Tips**:
                - Always store fabrics in a cool, dry place away from direct sunlight, as prolonged exposure can cause fading and deterioration.
                - Humidity can cause fabrics to degrade, so use moisture-absorbing packets or dehumidifiers in closets with high humidity.
            - **Delicate Fabrics**:
                - Use **garment bags** for delicate fabrics like **silk**, **wool**, and **lace** to prevent damage from dust, moths, or accidental snags.
                - For **wool** and other delicate fabrics, use padded hangers to avoid stretching out the fibers.
            - **Fabric-specific Storage**:
                - **Cotton**: Store cotton garments in a cool, dry place, and avoid storing them in plastic bags for long periods, as this can trap moisture.
                - **Linen**: Linen should be stored in a well-ventilated area, and it’s best to avoid storing it in drawers for too long to prevent musty odors from developing.
                - **Polyester**: Store polyester items in a place where they can breathe. While it is durable, it can be prone to static buildup in dry conditions, so consider using anti-static sheets.
                - **Silk**: Store silk garments in a cool, dry area away from other fabrics to avoid damage. Use padded hangers or fold silk clothing to avoid creases.
            
        - **Additional Fabric Care Tips**:
            - **Avoid Over-washing**: Fabrics like **denim** and **leather** should not be washed too frequently. Spot cleaning can often extend the lifespan of these materials.
            - **Ironing**: Always follow the care instructions on the label before ironing. Use the appropriate temperature setting for each fabric to avoid burning or damaging the fibers.
            - **Dealing with Stains**: 
                - **Oil Stains**: Use a stain remover or apply baking soda to absorb the oil before washing.
                - **Wine Stains**: Blot with cold water immediately, and use a mixture of white vinegar and dish soap to remove the stain.
                - **Ink Stains**: Apply rubbing alcohol to the stain and blot gently with a clean cloth.

        - **Best Practices for Long-lasting Fabrics**:
            - Regularly inspect fabrics for signs of wear and tear.
            - Repair minor damages, such as loose threads or small holes, as soon as they appear.
            - For wool and other natural fibers, consider using a fabric shaver to remove pilling, which can occur over time.

        By following proper care and maintenance instructions, you can ensure that your fabrics remain in great condition and last for years to come. Proper storage, cleaning, and maintenance can significantly extend the life of your favorite fabrics, saving you money and reducing waste.
        """)


        # Quiz 3: Identifying Fabric Use Cases
        st.subheader("Quiz: Identifying Fabric Use Cases")

        # Question 1
        question_1 = st.radio(
            "1. Which fabric is best suited for summer wear?", 
            ["Polyester", "Cotton", "Wool", "Silk"], 
            key="q1_module3"
        )

        # Question 2
        question_2 = st.radio(
            "2. How should you care for wool?", 
            ["Machine wash hot", "Dry clean only", "Line dry", "Iron at high heat"], 
            key="q2_module3"
        )

        # Question 3
        question_3 = st.radio(
            "3. Which fabric is commonly used for formal settings like suits and dresses?", 
            ["Denim", "Polyester", "Wool", "Cotton"], 
            key="q3_module3"
        )

        # Question 4
        question_4 = st.radio(
            "4. What is the best way to care for silk fabric?", 
            ["Machine wash on high heat", "Hand wash or dry clean", "Iron at high heat", "Hang dry in the sun"], 
            key="q4_module3"
        )

        # Question 5
        question_5 = st.radio(
            "5. Which fabric is most commonly used in activewear and sports clothing?", 
            ["Silk", "Cotton", "Polyester", "Wool"], 
            key="q5_module3"
        )

        # Submit Quiz
        if st.button("Submit Quiz 3 Answers", key="quiz3"):
            score = 0
            if question_1 == "Cotton":
                score += 1
            if question_2 == "Dry clean only":
                score += 1
            if question_3 == "Wool":
                score += 1
            if question_4 == "Hand wash or dry clean":
                score += 1
            if question_5 == "Polyester":
                score += 1
            
            st.success(f"You scored {score}/5 in this quiz!")
            
            # Next Steps for users with a high score
            if score >= 4:
                st.header("Next Steps")
                st.markdown("""
                Congratulations on completing **Module 3**! You've done a great job learning about fabric uses and care.  

                - **Next Steps**: Proceed to the **Intermediate Learning Path** to dive deeper into fabric properties and advanced techniques.  
                - **Explore Further**: Use the **Fabric Explorer** tool for hands-on learning and deeper exploration of fabric types and their uses.  

                Happy Learning!
                """)

# Run as a standalone app
if __name__ == "__main__":
    app()
