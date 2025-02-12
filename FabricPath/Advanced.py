import streamlit as st

def app():
    # Title and Overview
    st.title("Learning Path 3: Fabric Selection & Project Design (Advanced Level)")
    st.markdown("""
    ### Goal:
    Master fabric selection for complex design scenarios, considering durability, texture, and aesthetics.  
    **Duration**: 4-6 weeks  
    """)

    # Create tabs for each module
    tab1, tab2, tab3 = st.tabs(["Module 1: In-Depth Fabric Properties",
                                "Module 2: Fabric Selection for High-End Designs",
                                "Module 3: Sustainable Fabrics & Eco-Friendly Choices"])

    # Module 1: In-Depth Fabric Properties
    with tab1:
        st.header("Module 1: In-Depth Fabric Properties")

        st.subheader("Lesson 1.1: Fabric Durability and Texture Analysis")
        st.markdown("""
        ### Fabric Durability
        - **Definition**: Durability refers to a fabric's ability to withstand wear, pressure, and damage over time.
        - **Importance**:  
        - Vital for outerwear, upholstery, and garments subjected to frequent use.
        - Durable fabrics reduce the need for frequent replacements, making them cost-effective and sustainable.
        - **Examples**:  
        - **Denim**: Highly durable, suitable for heavy-duty applications like jeans and workwear. Its tightly woven structure makes it resistant to tears and abrasions.  
        - **Wool**: Known for its strength and elasticity. Used in coats, it resists wrinkles and retains warmth.  
        - **Polyester**: Blended for added durability in sportswear and jackets.  

        ### Fabric Texture Analysis
        - **Definition**: Texture describes the surface feel and appearance of a fabric, influencing its aesthetic appeal and comfort.
        - **Types of Texture**:  
        - **Smooth Textures**: Associated with luxury and elegance.  
            - Example: **Silk** for its glossy and soft feel, commonly used in evening wear and accessories.  
        - **Rough Textures**: Often used for rustic or casual designs.  
            - Example: **Burlap** or **Linen** for their earthy, coarse feel, popular in home décor or casual garments.  
        - **Soft and Plush Textures**: Ideal for cozy and comforting designs.  
            - Example: **Velvet** and **Fleece** for winter wear and upholstery.  

        ### Key Considerations
        - Matching durability and texture to the garment's purpose:
        - **Outerwear**: High durability and a soft or rugged texture (e.g., wool or tweed).
        - **Luxury Wear**: Smooth textures that convey elegance (e.g., silk or satin).
        - **Casual Wear**: Comfortable textures that balance durability and softness (e.g., cotton or linen).
        """)


        st.subheader("Lesson 1.2: Advanced Fabric Properties")
        st.markdown("""
        ### Key Properties of Fabrics

        - **Drape**:  
        - **Definition**: Refers to how a fabric hangs, flows, or conforms to shapes.  
        - **Importance**: Essential for designing garments like gowns, skirts, and draped tops.  
        - **Examples**:  
            - **Silk**: Excellent drape, flows gracefully, ideal for evening dresses.  
            - **Cotton**: Moderate drape, suited for structured casual wear.  
            - **Tweed**: Poor drape, used for stiff jackets and coats.

        - **Weight**:  
        - **Definition**: The heaviness of the fabric, usually measured in grams per square meter (GSM).  
        - **Importance**: Determines comfort, seasonality, and garment structure.  
        - **Examples**:  
            - **Lightweight Fabrics**:  
            - Examples: **Chiffon** and **Linen** for summer wear, providing breathability.  
            - **Heavyweight Fabrics**:  
            - Examples: **Wool** and **Canvas** for winter coats or utility items.  

        - **Hand (Feel)**:  
        - **Definition**: Describes the tactile sensation of fabric when touched.  
        - **Importance**: Critical for choosing fabrics for intimate wear, loungewear, and upholstery.  
        - **Examples**:  
            - **Soft Fabrics**:  
            - Example: **Velvet** for its luxurious and plush feel, often used in winter or formal wear.  
            - **Coarse Fabrics**:  
            - Example: **Canvas** for structured bags or utility garments.

        ---

        ### Case Study: Analyzing Fabric Behavior

        - **Objective**: Explore the real-world usability of two luxury fabrics: **Silk** and **Velvet**.  

        #### Silk:  
        - **Properties**:  
        - High drape, lightweight, smooth hand.  
        - Used in flowing garments like evening gowns and scarves.  
        - **Usability**:  
        - Pros: Luxurious appearance, soft feel.  
        - Cons: Requires special care (hand wash or dry clean).  

        #### Velvet:  
        - **Properties**:  
        - Low to moderate drape, medium to heavyweight, plush hand.  
        - Commonly used in jackets, evening dresses, and home décor.  
        - **Usability**:  
        - Pros: Rich texture, visually appealing for formal wear.  
        - Cons: Prone to crushing; requires careful storage and handling.  

        - **Insights**:  
        - Silk excels in lightweight, draped designs but requires maintenance.  
        - Velvet is better for structured designs with rich textures, making it suitable for colder weather and luxury interiors.  
        """)


        # Quiz 1
        st.subheader("Quiz: Matching Fabric to Project")
        question_1 = st.radio(
            "1. Which property is most important for selecting fabric for a gown?", 
            ["Durability", "Drape", "Weight", "Texture"], key="q1_module1"
        )
        question_2 = st.radio(
            "2. What is the best choice for structured outerwear?", 
            ["Velvet", "Denim", "Silk", "Jute"], key="q2_module1"
        )

        if st.button("Submit Quiz 1 Answers", key="quiz1"):
            score = 0
            if question_1 == "Drape":
                score += 1
            if question_2 == "Denim":
                score += 1
            st.success(f"You scored {score}/2 in this quiz!")

    # Module 2: Fabric Selection for High-End Designs
    with tab2:
        st.header("Module 2: Fabric Selection for High-End Designs")

        # Lesson 2.1: Choosing Fabrics for Luxury and High-Detail Designs
        st.subheader("Lesson 2.1: Choosing Fabrics for Luxury and High-Detail Designs")
        st.markdown("""
        - **Luxury Fabrics**:  
        - **Silk**:  
            - Characteristics: Soft, shiny, and elegant. Ideal for high-end garments like evening gowns, bridal dresses, and luxurious scarves.  
            - Best for: Formal wear, bridal couture, and any garment where a glossy, refined appearance is desired.  
            - Care: Dry clean only to maintain its sheen and texture.  
        - **Cashmere**:  
            - Characteristics: Warm, lightweight, and incredibly soft. Known for its luxurious feel and insulation properties.  
            - Best for: Tailored coats, knitwear, and high-end sweaters or scarves.  
            - Care: Gentle hand wash or dry clean. Avoid exposure to high heat to preserve softness.  
        - **Satin**:  
            - Characteristics: Smooth, glossy surface with a rich sheen. Offers a sophisticated and opulent look.  
            - Best for: Evening wear, prom dresses, or any garment that needs to reflect light for a high-impact visual effect.  
            - Care: Dry clean only, as satin can be delicate.  

        - **Choosing the Right Fabric for Luxury Designs**:  
        - **Consider Drape and Weight**: For luxurious gowns, opt for fabrics with a soft drape, such as silk or satin, which move fluidly and provide an elegant appearance.  
        - **Texture and Feel**: A smooth texture like satin or cashmere offers a sense of luxury, while silk provides a timeless, refined feel perfect for high-end occasions.  
        - **Durability and Care**: Ensure that the fabric selected aligns with the maintenance expectations for high-end garments—delicate fabrics require special attention to preserve their appearance.

        """)

        # Lesson 2.2: Mixing Fabrics for Function and Aesthetics
        st.subheader("Lesson 2.2: Mixing Fabrics for Function and Aesthetics")
        st.markdown("""
        - **Blending for Purpose**:  
        - **Wool-Silk Blends**:  
            - Characteristics: Wool provides warmth and structure, while silk adds smoothness and sheen. This combination is ideal for garments that need both functionality (insulation) and luxury (smooth finish).  
            - Best for: Luxury outerwear, high-end coats, and tailored suits where both warmth and elegance are required.  
        - **Polyester-Cotton Blends**:  
            - Characteristics: Combines the natural breathability of cotton with the durability and wrinkle-resistance of polyester.  
            - Best for: Casual yet polished luxury pieces like blouses or dresses with a structured finish but comfortable feel.  
        - **Silk-Linen Blends**:  
            - Characteristics: Silk offers shine and softness, while linen adds a cool, breathable quality. This blend is perfect for summer high-end fashion, providing elegance while maintaining comfort.  
            - Best for: Lightweight luxury dresses, summer blouses, and trousers.  
        - **Cashmere-Wool Blends**:  
            - Characteristics: A mix that combines the luxurious softness of cashmere with the warmth and structure of wool.  
            - Best for: High-end knitwear, coats, and cardigans that need to provide both warmth and luxury without being too bulky.

        - **Example Use Case: Mixing Fabrics for Luxury Outerwear**:  
        - **Luxury Coat**:  
            - Combining a wool exterior for durability and warmth with a silk lining for a luxurious feel.  
            - The silk lining enhances the overall comfort, allowing the coat to feel smooth against the skin, while the wool outer layer maintains structure and provides the necessary insulation.  
            - **Why this works**: Wool provides strength and practicality, while the silk lining offers elegance and an elevated tactile experience.

        - **Aesthetic Considerations**:  
        - **Texture and Visual Appeal**: Combining fabrics with different textures creates depth and interest in luxury designs. For example, a satin overlay on a wool base can create visual contrast and sophistication.  
        - **Harmonizing Fabrics**: Blending fabrics should also consider color harmony and finish. A matte wool exterior combined with a glossy silk lining can offer both a visual and tactile contrast, which enhances the garment's overall luxurious feel.

        """)


        # Quiz 2
        st.subheader("Quiz: Fabric for High-End Designs")

        # Question 1: Luxury evening gown fabric
        question_1 = st.radio(
            "1. What is the ideal fabric for a luxury evening gown?", 
            ["Cotton", "Silk", "Denim", "Canvas"], key="q1_module2"
        )

        # Question 2: Fabric combination for a luxury coat
        question_2 = st.radio(
            "2. What fabric combination is best for a luxury coat?", 
            ["Cotton-Polyester", "Wool-Silk", "Linen-Jute", "Velvet-Satin"], key="q2_module2"
        )

        # Question 3: Best fabric for structured outerwear
        question_3 = st.radio(
            "3. Which fabric is most suitable for a structured winter jacket?", 
            ["Tweed", "Chiffon", "Linen", "Satin"], key="q3_module2"
        )

        # Question 4: Key property of velvet in design
        question_4 = st.radio(
            "4. What is a notable property of velvet that makes it ideal for formal wear?", 
            ["Breathability", "Plush texture", "Lightweight", "Wrinkle resistance"], key="q4_module2"
        )

        # Question 5: Best option for a summer formal suit
        question_5 = st.radio(
            "5. Which fabric would be most appropriate for a summer formal suit?", 
            ["Silk", "Linen", "Velvet", "Canvas"], key="q5_module2"
        )

        # Quiz Submission
        if st.button("Submit Quiz 2 Answers", key="quiz2"):
            score = 0

            # Answer validations
            if question_1 == "Silk":
                score += 1
            if question_2 == "Wool-Silk":
                score += 1
            if question_3 == "Tweed":
                score += 1
            if question_4 == "Plush texture":
                score += 1
            if question_5 == "Linen":
                score += 1

            # Display results
            st.success(f"You scored {score}/5 in this quiz!")

            # Feedback based on performance
            if score == 5:
                st.header("Excellent!")
                st.markdown("""
                - You have a strong understanding of fabric selection for high-end designs.  
                - Proceed to the next module to further enhance your expertise.  
                """)
            elif 3 <= score < 5:
                st.markdown("""
                - Good job! Review the lessons to refine your knowledge and aim for a perfect score.  
                - You can move on, but consider revisiting key concepts for better mastery.  
                """)
            else:
                st.error("""
                - It seems you need to revisit Module 2.  
                - Go through the lessons again to solidify your understanding of luxury fabrics.  
                """)

    # Module 3: Sustainable Fabrics & Eco-Friendly Choices
    with tab3:
        st.header("Module 3: Sustainable Fabrics & Eco-Friendly Choices")

        st.subheader("Lesson 3.1: Introduction to Sustainable Fabrics")
        st.markdown("""
        - **Why Choose Sustainable Fabrics?**  
        - Reduces environmental impact by minimizing waste and pollution.  
        - Supports ethical farming and fair trade practices.  
        - Promotes long-term conservation of natural resources.

        - **Eco-Friendly Fabric Options**:  
        - **Organic Cotton**:  
            - Grown without synthetic fertilizers or pesticides.  
            - Uses less water compared to conventional cotton.  
            - Soft, breathable, and hypoallergenic.  
            - Ideal for: T-shirts, baby clothes, and bedding.
            
        - **Hemp**:  
            - One of the strongest and most durable natural fibers.  
            - Requires minimal water and pesticides to grow.  
            - Naturally resistant to UV rays and mold.  
            - Ideal for: Bags, ropes, jeans, and eco-friendly activewear.
            
        - **Jute**:  
            - Affordable, versatile, and 100% biodegradable.  
            - Grown in high-rainfall areas without the need for irrigation.  
            - Used in: Tote bags, upholstery, and home decor.  

        - **Advantages of Sustainable Fabrics**:  
        - Helps combat climate change by reducing carbon emissions.  
        - Protects ecosystems by minimizing harmful agricultural practices.  
        - Supports ethical working conditions for farmers and workers.

        - **Challenges**:  
        - Higher cost due to organic farming and ethical production.  
        - Limited availability compared to conventional fabrics.  
        - Requires consumer awareness and demand to drive adoption.
        """)

        st.subheader("Lesson 3.2: Fabric Life Cycle and Environmental Impact")
        st.markdown("""
        - **Fabric Life Cycle**:  
        - The life cycle of a fabric consists of several stages, each with its own environmental impact:  
            - **Production**:  
            - This stage involves growing or manufacturing the raw materials (e.g., cotton, hemp, polyester).  
            - Environmental impact: High water consumption (e.g., cotton), chemical use (e.g., dyes, pesticides), and energy use (e.g., polyester production).  
            - Sustainable practices: Organic farming, using renewable energy sources, and reducing water consumption.
            
            - **Usage**:  
            - Fabrics are used for their intended purpose, such as clothing, home textiles, or industrial products.  
            - Environmental impact: Frequent washing, drying, and ironing can contribute to energy consumption and fabric degradation.  
            - Sustainable practices: Reducing washing frequency, air drying, and using low-energy appliances.

            - **Disposal**:  
            - The end of the fabric's life involves disposal, which can lead to significant environmental harm if not managed properly.  
            - Environmental impact: Non-biodegradable fabrics (e.g., polyester) can sit in landfills for hundreds of years, while others like cotton and hemp decompose more easily.  
            - Sustainable practices: Recycling fabrics, donating old clothes, or upcycling them into new products.

        - **Environmental Footprint Considerations**:  
        - The environmental footprint of fabric production can vary greatly depending on the materials used and the processes employed.  
        - It’s important to consider the entire life cycle of the fabric, from raw material extraction to disposal, when assessing its sustainability.  

        - **Best Practices for Reducing Environmental Impact**:  
        - **Opt for Recyclable Fabrics**: Choose fabrics that can be reused or recycled at the end of their life cycle, such as recycled polyester, wool, and cotton.  
        - **Choose Compostable Fabrics**: Organic fabrics like cotton, hemp, and jute are biodegradable and break down naturally, minimizing landfill waste.  
        - **Reduce Textile Waste**: Avoid overconsumption and encourage practices like buying durable, long-lasting fabrics that won’t need frequent replacement.  
        - **Support Ethical Brands**: Choose brands that use environmentally friendly production methods and sustainable fabrics, supporting the transition toward a circular economy.

        - **The Importance of Conscious Consumption**:  
        - The choices we make as consumers impact the fabric industry. By being mindful of the fabrics we buy and how we care for them, we can significantly reduce the environmental burden of textiles.
        """)


        # Quiz 3
        st.subheader("Quiz: Sustainable Fabric Knowledge")
        # Question 1
        question_1 = st.radio(
            "1. Which of the following fabrics is considered the most eco-friendly due to its minimal water usage and biodegradability?", 
            ["Polyester", "Jute", "Silk", "Velvet"], key="q1_module3"
        )

        # Question 2
        question_2 = st.radio(
            "2. What is a key environmental benefit of using organic cotton over conventional cotton?", 
            ["It is more durable", "It requires less water to grow", "It is produced without synthetic chemicals", "It has a higher production cost"], 
            key="q2_module3"
        )

        # Question 3
        question_3 = st.radio(
            "3. Which of the following is a sustainable practice for polyester fabrics?", 
            ["Use only polyester for activewear", "Choose polyester made from recycled materials", "Avoid washing polyester garments", "Choose polyester for all types of clothing"], 
            key="q3_module3"
        )

        # Question 4
        question_4 = st.radio(
            "4. What is the major environmental concern with synthetic fibers like polyester?", 
            ["They are biodegradable", "They require minimal energy to produce", "They do not decompose easily in landfills", "They are made from natural resources"], 
            key="q4_module3"
        )

        # Question 5
        question_5 = st.radio(
            "5. Which sustainable fabric grows without the use of synthetic pesticides or fertilizers?", 
            ["Hemp", "Wool", "Polyester", "Silk"], 
            key="q5_module3"
        )

        # Quiz Submission
        if st.button("Submit Quiz 3 Answers", key="quiz3"):
            score = 0
            if question_1 == "Jute":
                score += 1
            if question_2 == "It is produced without synthetic chemicals":
                score += 1
            if question_3 == "Choose polyester made from recycled materials":
                score += 1
            if question_4 == "They do not decompose easily in landfills":
                score += 1
            if question_5 == "Hemp":
                score += 1

            # Display Quiz Results
            st.success(f"You scored {score}/5 in this quiz!")
            if score == 5:
                st.header("Final Advice")
                st.markdown("""
                - Congratulations on completing the **Advanced Learning Path**!  
                - To further enhance your expertise:  
                - Use the **Fabric Explorer** to test fabric properties, compare materials, and make data-driven decisions.  
                - Chat with **Fabrica**, your intelligent fabric assistant, for tailored recommendations based on your specific project needs or preferences.  
                - Stay creative and informed as you design with fabrics!  

                **Happy Learn!**
                            """)


# Run as a standalone app
if __name__ == "__main__":
    app()
