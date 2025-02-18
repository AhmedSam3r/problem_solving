# Notes
## ThreeSum
- threeSum is a tricky problem, it taught me to break down the problem into smaller ones
- while checking the smaller problem, try to identify a pattern for it which can help you solve the overall problem like TwoSumSorted
- try to visualize and understand the problem visually and mathemtically, this can help ex: a+b+c=0

## ContainerMostWater
In the two-pointer approach for solving the container problem, you aim to maximize the water stored between two bars by strategically moving the pointers. Here's how the approach ensures that no larger area combination is overlooked:

### Key Insights:
1. **Initial Setup**:
   - You start with two pointers: one at the beginning (`left`) and one at the end (`right`) of the array.
   - The area is calculated as \( \text{width} \times \min(\text{height}[left], \text{height}[right]) \).

2. **Why Move the Smaller Pointer**:
   - The height of the container is determined by the shorter of the two bars (`height[left]` or `height[right]`).
   - To maximize the area, you want to find a taller bar that could increase the height of the container.
   - If you move the taller bar, the height will either decrease or stay the same, and the width will decrease, leading to a smaller or equal area.
   - By moving the pointer of the shorter bar, you give a chance to find a taller bar that might increase the height and potentially increase the area despite the decreasing width.

3. **Ensuring No Larger Area is Missed**:
   - **Height Consideration**: Moving the pointer of the shorter bar allows for potential increases in the minimum height, which is critical for maximizing the area.
   - **Width Consideration**: The area is dependent on both height and width. As you reduce the width (by moving pointers), you aim to compensate by increasing the minimum height.
   - **Systematic Exploration**: By always moving the pointer pointing to the shorter bar, you systematically explore all potential combinations that could lead to a larger area.

### Why This Works:
- The two-pointer method efficiently narrows down the possible combinations by leveraging the fact that any combination involving the current taller bar and another shorter or equal bar will not yield a greater area than the current maximum.
- This approach ensures that you explore all meaningful possibilities without redundant calculations, thus covering all potential maximum areas.

This strategy leverages both height and width dynamics effectively, ensuring that you do not miss out on any larger area combinations as you converge towards the center of the array.