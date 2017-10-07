<b>a. verify that their Null and alternative hypotheses are formulated correctly</b>

The general notion being tested is is that "women riding time is less than men riding time." The exact null hypothesis stated is "Women riding time is more than or the same of Men riding time." Generally, this is correct, but I would rephrase the null hypothesis to be more precise about the measurements.

For example,<br>
<b>H0</b>: The average duration of a ride in seconds is at least as high or or higher for female riders than male riders.
<br><b>H1</b>: The average duration of a ride in seconds is higher is lower for female riders than male riders.

<b>b. verify that the data supports the project</b>

The repo adds a new column to measure the ride duration in seconds and uses a dictionary to map the qualitative gender name to integers (1 for male, 2 for male). Two changes I would recommnend - dropping the Age field (not necessary for the analysis) and dropping records where the gender is Unknown.

<b>c. chose an appropriate test to test H0 given the type of data, and the question asked</b>

Using the guidance from "How to choose the right statistical test?" (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/), the first point of guidance is:
<br><br>
<i>Question 1: Is there a difference between groups that are unpaired? Groups or data sets are regarded as unpaired if there is no possibility of the values in one data set being related to or being influenced by the values in the other data sets. Different tests are required for quantitative or numerical data and qualitative or categorical data as shown in Fig. 1.</i>

For this hypothesis test, the groups are unpaired, and I proceed to Figure 1, which first distinguishes between numerical and categorical data. We are measuring the time duration of rides - clearly numerical data. The next point of difference is whether the data is parametric or not. Using the guidance here (http://vassarstats.net/textbook/parametric.html) to ponder our assumptions about the normal distribution of the source population, I conclude that the data is parametric and select the <b>2 groups unpaired t-test</b>.

One other note about the hypothesis itself - the duration of a ride is an indirect measure of the distance of the ride. It would be a more interesting hypothesis, in my opinion, to test whether there is a significant difference in the <it>speed</it> of male vs. female riders. Duration would be needed for this, as well as the distance riders went. We don't have the actual distances, but we do have the coordinates of the starting and ending stations. From this, a distance could be hypothetically inferred, and from that, the speed for men versus women.
