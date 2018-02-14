#####################
### CROSS PRODUCT ###
#####################

cross_product_template = ['{part1} {part2}']

cross_product_switches = {
    'part1': [
        "For two vectors, taking the cross product produces another vector which is perpendicular to the two vectors and has length equal to the area of the parallelogram whose sides are formed by that pair of vectors.",
        "Taking the cross product of two vectors results in another vector which is perpendicular to the two vectors and whose norm is equal to the area of the parallelogram spanned by those two vectors.",
        "The cross product of a pair of vectors yields another vector which is not only perpendicular to the pair, but also whose magnitude equals the area of the parallelogram whose sides are formed by pair.",
        "The cross product of two vectors results in another vector which is perpendicular to the two vectors and also has magnitude equal to the area of the parallelogram whose sides consist of those two vectors."
    ],
    "part2": [
        "The cross product is given by the formula {eq}\\langle u_1, u_2, u_3 \\rangle \\times \\langle v_1, v_2, v_3 \\rangle = \\langle u_2v_3 - u_3v_2, u_3v_1 - u_1v_3, u_1v_2 - u_2v_1 \\rangle{/eq}.",
        "The computation is given by the formula {eq}\\langle u_1, u_2, u_3 \\rangle \\times \\langle w_1, w_2, w_3 \\rangle = \\langle u_2w_3 - u_3w_2, u_3w_1 - u_1w_3, u_1w_2 - u_2w_1 \\rangle{/eq}.",
         "The formula for the cross product is {eq}\\langle a_1, a_2, a_3 \\rangle \\times \\langle b_1, b_2, b_3 \\rangle = \\langle a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 -a_2b_1 \\rangle{/eq}.",
         "The formula is given by {eq}\\langle x_1, x_2, x_3 \\rangle \\times \\langle y_1, y_2, y_3 \\rangle = \\langle x_2y_3 - x_3y_2, x_3y_1 - x_1y_3, x_1y_2 - x_2y_1 \\rangle{/eq}."
    ]
}

######################
### LINE INTEGRALS ###
######################

line_integrals_template = ['{Line integrals can be computed as separate integrals over each of the segments} {For each segment, it is easiest to parameterize the variables and write all of the variables and differentials in terms of the parameter} {This way, the entire integral may be written in terms of the parameter, causing it to simplify to a single-variable integral}']
line_integrals_switches = {
    'Line integrals can be computed as separate integrals over each of the segments': [
        'Line integrals can be computed as separate integrals over each of the segments.',
        'Line integrals are computed as separate integrals over each of the segments.',
        'Line integrals are computed separately over each of the segments.',
        "A line integral's path can be broken up into segments, and the integral can be computed separately over these segments.",
        "Once a line integral's path is broken up into segments, the integral can be computed separately over these segments.",
        "After a line integral's path is broken up into segments, the integral can be evaluated separately over these segments.",
        "After breaking up the path of a line integral into segments, the integral can be evaluated separately over the segments.",
        "After breaking up the path of a line integral into segments, the integral can be computed separately over each of the segments.",
        "Line integrals can be broken up over multiple segments.",
        "Line integrals can be broken up and evaluated over multiple segments.",
        "Line integrals can be separated over multiple segments.",
        "Line integrals can be separated and evaluated over multiple segments."
    ],
    'For each segment, it is easiest to parameterize the variables and write all of the variables and differentials in terms of the parameter': [
        'For each segment, it is easiest to parameterize the variables and write all of the variables and differentials in terms of the parameter.',
        'Along each segment, then, it is possible to write the equation of the line in terms of a parameter and express the integrals in terms of that parameter.',
        'One can write the variables in terms of a parameter along each segment, and take differentials in terms of the parameter too.',
        'Each segment can be expressed as a line with a single parameter, so the integrals can written in terms of that parameter.'
    ],
    'This way, the entire integral may be written in terms of the parameter, causing it to simplify to a single-variable integral': [
        'This way, the entire integral may be written in terms of the parameter, causing it to simplify to a single-variable integral.',
        'Writing everything in terms of the parameter will simplify the integral into a single-variable integral.',
        'The line integral can be transformed into a single-variable integral by expressing all of the integrals in terms of the same parameter.',
        'Then, the entire integral can be simplified into a single-variable integral by writing everything in terms of the parameter.',
        'Writing all the integrals in terms of a single parameter, the entire line integral can be simplified into a single-variable integral.'
    ]
}

############################
### LAGRANGE MULTIPLIERS ###
############################

lagrange_multipliers_template = ["{intro} {body} {formula}"]
lagrange_multipliers_switches = {
    "intro": [
        "In optimization problems, we wish to optimize a function ''f'' subject to a constraint that some other function ''g'' has a fixed value ''k''.",
        "In applications, when we want to maximize or minimize a function ''f'', there is often a constraint that some other function ''g'' (which represents some kind of resource) must be held at a constant value ''k''.",
        "When we want to maximize or minimize a function ''f'', as is necessary in optimization problems, we often have to also fulfill another constraint that some function ''g'' has a fixed value ''k''.",
        "Optimization problems often involve finding the minimum or maximum of a function ''f'' subject to the constraint that another function ''g'' must have a fixed value ''k''."
    ],
    "body": [
        "The method of Lagrange multipliers leverages the fact that, when ''f'' attains an optimum, its gradient must be parallel to that of ''g''.",
        "Lagrange multipliers involves exploiting the fact that the gradient of ''f'', evaluated at a point which is a maximum or minimum of ''f'', is parallel to the gradient of ''g'' at that same point.",
        "It happens that when ''f'' is optimized, its gradient is parallel to that of ''g''. Lagrange multipliers leverages this fact.",
        "When ''f'' attains a maximum or minimum, the gradients of ''f'' and ''g'' are parallel. This fact is the main insight utilized by Lagrange multipliers."
    ],
    "formula": [
        "That is, {eq} \\nabla f = \\lambda \\nabla g {/eq} for some constant {eq}\\lambda{/eq}.",
        "Symbolically, for some constant {eq}\\lambda{/eq}, we have {eq} \\nabla f = \\lambda \\nabla g {/eq}.",
        "In formal notation, there is some constant {eq}\\lambda{/eq} such that {eq} \\nabla f = \\lambda \\nabla g {/eq}.",
        "Thus, for some constant {eq}\\lambda{/eq}, it must be true that {eq} \\nabla f = \\lambda \\nabla g {/eq}.",
        "Thus, it must be true that {eq} \\nabla f = \\lambda \\nabla g {/eq} for some constant {eq}\\lambda{/eq}."
    ]
}

#########################################
### SEPEARABLE DIFFERENTIAL EQUATIONS ###
#########################################

separable_differential_equations_template = ["{part1} {part2}"]
separable_differential_equations_switches = {
    "part1": [
        "A differential equation is said to be separable if it can be manipulated so that the variables and their respective differentials become separated on either side of the equation.",
        "A separable differential equation is one where the variables and differentials can be separated on either side of the equation.",
        "A differential equation is separable when it can be rearranged so that each side contains an expression of a single variable and its differential.",
        "Separable differential equations are those which can be manipulated so that each side gets its own variable and respective differential.",
        "A differentiable equation which can be manipulated so that each side contains a single-variable expression and differential is said to be separable.",
    ],
    "part2": [
        "After separating the variables and their respective differentials on either side of the equation, one can find the solution by integrating both sides of the equation.",
        "Once the variables and differentials are separated, one can solve by integrating both sides.",
        "One can integrate both sides once the equation has been separated.",
        "The solution is found by integrating both sides after the variables and their respective differentials have been separated.",
        "After the equation is separated, one can integrate both sides to find the solution."
    ]
}

###################
### DOT PRODUCT ###
###################

dot_product_template = ["{part1} {part2}"]
dot_product_switches = {
    "part1": [
        "The dot product measures the projection of one vector onto another and can be used to tell whether two vectors are orthogonal.",
        "The dot product quantifies the overlap of two vectors and can be used to tell whether two vectors are orthogonal..",
        "The projection of one vector onto another can be quantified by the dot product. It can also be used to tell whether two vectors are orthogonal.",
        "The overlap of one vector onto another can be measured by the dot product. It can also be used to tell whether two vectors are orthogonal.",
        "The dot product measures the degree to which two vectors overlap and can be used to tell whether two vectors are orthogonal.",
        "The dot product quantifies the degree to which a vector projects onto another vector and can be used to tell whether two vectors are orthogonal."
    ],
    "part2": [
        "The most familiar way to calculate it is by summing the products of corresponding components, but another way uses the magnitudes of the vectors and the angle between them: \n{eq} a\\cdot b = |a||b|\\cos \\theta {/eq} \n where {eq} \\theta {/eq} is the angle between the two vectors.",
        "The dot product can be calculated using the formula {eq} a\\cdot b = |a||b|\\cos \\theta {/eq} where {eq} \\theta {/eq} is the angle between the two vectors, or by summing the products of corresponding components.",
        "The dot product can be calculated two different ways. The first is to use the rule {eq} a\\cdot b = |a||b|\\cos \\theta {/eq} where {eq} \\theta {/eq} is the angle between the two vectors, and the second is to sum the products of corresponding components.",
        "One way to calculate the dot product is to use the rule {eq} a\\cdot b = |a||b|\\cos \\theta {/eq} where {eq} \\theta {/eq} is the angle between the two vectors. Another way is to sum the products of corresponding components."
    ]
}

##################################
### INITIAL CONDITION PROBLEMS ###
##################################

initial_condition_problems_template = ["{part1} {part2} {part3} {part4}"]
initial_condition_problems_switches = {
    "part1": [
        "Sometimes, we can work backwards from a function's derivative to find the function itself.",
        "If we know a function's derivative, we can find the function by taking the antiderivative.",
        "If we know a function's derivative, we can find the function by taking the indefinite integral.",
        "The antiderivative can be used to find a function, given its derivative.",
        "The indefinite integral can be used to find a function, given its derivative."
    ],
    "part2": [
        "However, when we take an antiderivative, we are left with an constant of integration.",
        "But an unknown constant of integration arises whenever we take an antiderivative.",
        "Whenever we take an antiderivative, though, an unknown constant of integration arises.",
        "However, when we take an indefinite integral, we are left with an constant of integration.",
        "But an unknown constant of integration arises whenever we take an indefinite integral.",
        "Whenever we take an indefinite integral, though, an unknown constant of integration arises."
    ],
    "part3": [
        "For this reason, we need more information about the function, such as its value at a particular point.",
        "Consequently, more information about the function is needed, like a point which it contains.",
        "In order to find the constant, we need to know the function's value at some point.",
        "Some other constraint must be placed on the funcion, in order to fix the constant."
    ],
    "part4": [
        "This additional information is known as an initial condition.",
        "Such a constraint is known as an initial condition.",
        "Such information is known as an initial condition."
    ]
}

############################
### EQUATION OF A SPHERE ###
############################

equation_of_a_sphere_template = ["{part1} {part2}"]
equation_of_a_sphere_switches = {
    "part1": [
        "If we know a sphere's center and its radius, we can write its equation.",
        "A sphere's full equation can be written, knowing its center and radius.",
        "A sphere's center and radius can be used to write its full equation.",
        "The center and radius of a sphere are needed to write its full equation.",
        "To write the equation for a sphere, one needs to know its center and radius."
    ],
    "part2": [
        "For a sphere with center {eq}(a,b,c){/eq} and radius {eq}r{/eq}, the equation is given by {eq}(x-a)^2+(y-b)^2+(z-c)^2=r^2{/eq}.",
        "The equation {eq}(x-a)^2+(y-b)^2+(z-c)^2=r^2{/eq} describes a sphere with center {eq}(a,b,c){/eq} and radius {eq}r{/eq}.",
        "For a sphere with center {eq}(A,B,C){/eq} and radius {eq}R{/eq}, the equation is given by {eq}(x-A)^2+(y-B)^2+(z-C)^2=R^2{/eq}.",
        "The equation {eq}(x-A)^2+(y-B)^2+(z-C)^2=R^2{/eq} describes a sphere with center {eq}(A,B,C){/eq} and radius {eq}R{/eq}.",
        "If the center is {eq}(x_0,y_0,z_0){/eq} and radius {eq}r{/eq}, the equation is given by {eq}(x-x_0)^2+(y-y_0)^2+(z-z_0)^2=r^2{/eq}.",
        "The equation {eq}(x-x_0)^2+(y-y_0)^2+(z-z_0)^2=r^2{/eq} describes a sphere with center {eq}(x_0,y_0,z_0){/eq} and radius {eq}r{/eq}."
    ]
}

###############################
### DIRECTIONAL DERIVATIVES ###
###############################

directional_derivatives_template = ["{part1} {part2} {part3}"]
directional_derivatives_switches = {
    "part1": [
        "The gradient of a function is a vector that is obtained by taking the function's partial derivatives component-wise.",
        "Taking the partial derivatives of a function and assigning them as components of a vector yields the function's gradient.",
        "For a function {eq}f(x,y,z){/eq}, the gradient is given by {eq}\langle f_x, f_y, f_z \rangle{/eq}.",
        "The gradient of a function {eq}f(x,y,z){/eq} is the vector {eq}\langle f_x, f_y, f_z \rangle{/eq}.",
        "Computing the partial derivatives of a function {eq}f(x,y,z){/eq} and assigning them as components of a vector produces the gradient of the function."
    ],
    "part2": [
        "It gives the direction of greatest increase of the function, and its magnitude gives the magnitude of that increase.",
        "The gradient gives the direction of greatest increase of the function, and its magnitude gives the magnitude of that increase.",
        "It gives the magnitude and direction of greatest increase of the function.",
        "The gradient gives the magnitude and direction of greatest increase of the function.",
        "The gradient's magnitude and direction are those of greatest increase of the function.",
        "Its magnitude and direction are those of greatest increase of the function."
    ],
    "part3": [
        "To find the magnitude of increase in a different direction, one can simply take the dot product of the gradient with the new direction vector.",
        "The magnitude of increase in another direction can be computed as the dot product of the new direction vector with the gradient.",
        "In a different direction, the magnitude of increase is computed as the dot product of the gradient and the direction vector.",
        "The dot product of the gradient and another direction vector computes the magnitude of increase in the other direction.",
        "Taking the dot product of a different direction vector and the gradient gives the magnitude of increase in the new direction."
    ]
}

###########################
### INDEFINITE INTEGRAL ###
###########################

indefinite_integrals_template = ["{part1} {part2}"]
indefinite_integrals_switches = {
    "part1": [
        "The indefinite integral of a function is the function whose derivative is the function within the integral. For this reason, it is sometimes called the antiderivative.",
        "The indefinite integral of a function is the function whose derivative is the function within the integral. For this reason, it is sometimes called the antiderivative.",
        "The indefinite integral is sometimes called the antiderivative, because it is the opposite of differentiation. Instead of taking the derivative of the integrand, we work backwards to figure out which function has the integrand as its derivative.",
        "Integrating is the opposite of differentiating. Instead of taking the derivative of the integrand, we work backwards to figure out which function has the integrand as its derivative.",
        "Integrals are sometimes called antiderivatives because in an integral, we work backwards to figure out which function has the integrand as its derivative."
    ],
    "part2": [
        "Since the derivative of any constant is zero, the indefinite integral is unique up to a constant, called the constant of integration.",
        "Since constants vanish under the derivative, the solution to the indefinite integral will include an unknown constant, called the constant of integration.",
        "The solution to the indefinite integral will include a constant of integration, an unknown constant that is needed because the derivative of any constant is zero.",
        "The finishing touch on the solution to an indefinite integral is the constant of integration, an arbitrary constant that is included becuase constants vanish under the derivative."
    ]
}

#####################
### TANGENT LINES ###
#####################

tangent_lines_template = ["{part1} {part2}"]
tangent_lines_switches = {
    "part1": [
        "The tangent line to a curve at a point is the line which passes through that point with the same slope as the function at that point.",
        "For a given point on a given curve, the tangent line at that point is the line which passes through that point and has the same slope as the function at that point.",
        "The tangent line to a function at a given point has the same slope as the function at that point.",
        "The line which intersects a function at a given point and has the same slope as the function at that point is called the tangent line."
    ],
    "part2": [
        "To find the slope of the function, we can simply take the derivative and evaluate the derivative at the given point.",
        "We can use the derivative of the function to find its slope at the given point.",
        "Using the function's derivative, we can find the slope of the tangent line.",
        "We can find the slope of the tangent line by evaluating the function's derivative at the given point.",
        "In order to find the slope of the tangent line, we can take the derivative of the function and evaluate it at the given point."
    ]
}

####################################
### DERIVATIVE AS RATE OF CHANGE ###
####################################

derivative_as_rate_of_change_template = ["{part1} {part2} {part3}"]
derivative_as_rate_of_change_switches = {
    "part1": [
        "The derivative of a function can be interpreted as the rate of change of a function per unit of input.",
        "If we want to find the rate of change of a function per unit of input, we can take its derivative.",
        "To find the rate of change of a function, we can use the derivative, which may be interpreted as the rate of change per unit input.",
        "The derivative of a function gives its rate of change per unit input.",
        "A function's derivative tells how the function changes in response to an increase in one unit input."
    ],
    "part2": [
        "Since the derivative is itself a function, the rate of change may depend upon the function variables as well.",
        "The rate of change may depend upon the function variables, since the derivative is itself a function.",
        "The derivative is a function itself, so the rate of change may depend upon the function variables as well."
    ],
    "part2": [
        "Thus, if we want to find the rate of change of some quantity, and we can describe that quantity as a function, we don't need to do any experiments to find the rate of change.",
        "Thus, it is not necessary to do any more experiments to find rate of change if we know how to express the quantity in question as a function -- we can work it all out on paper.",
        "Consequently, if we can express some quantity as a function, we can work out its rate of change on paper without having to do any experiments."
    ]
}

######################
### TANGENT PLANES ###
######################

tangent_planes_template = ["{part1} {part2} {part3}"]
tangent_planes_switches = {
    "part1": [
        "The standard normal vector for a plane is given by the coefficients on the variables.",
        "The coefficients on the variables in the equation for a plane are the components of its standard normal vector.",
        "If one assigns the variable coefficients in an equation for a plane as components in a vector, that vector will be perpendicular to the plane. Moreover it is called the plane's standard normal vector."
    ],
    "part2": [
        "Also, since the gradient of a function is always perpendicular to its level curve, the gradient is always perpendicular to its tangent plane.",
        "Also, the gradient of a function is always perpendicular to the function's tangent plane, since the gradient of a function is always perpendicular to its level curve.",
        "Also, the gradient of a function, being perpendicular to the function's level curves, is thus perpendicular to its tangent plane."
    ],
    "part3": [
        "Therefore, the tangent plane for a level curve has as its coefficients the partial derivatives of the function.",
        "Thus, to find the tangent plane for a function, we can simply use the partial derivatives as the variable coefficients.",
        "Consequently, one can use partial derivatives as the variable coefficients when constructing the tangent plane to a function."
    ]
}

########################
### L'HOPITAL'S RULE ###
########################

lhopitals_rule_template = ["{part1} {part2} {part3}"]
lhopitals_rule_switches = {
    "part1": [
        "L'Hopital's rule can be be used to find limits which take indeterminate form of 0 divided by 0 or infinity divided by infinity.",
        "When substitution would cause a limit to go to 0 divided by 0 or infinity divided by infinity, it is said to be of indeterminate form, and L'Hopital's rule can be applied.",
        "A limit which goes to 0 divided by 0 or infinity divided by infinity is said to be of indeterminate form. In these limits, L'Hopital's rule applies.",
        "L'Hopital's rule applies to limits which are indeterminate in the sense that they go to 0 divided by 0 or infinity divided by infinity.",
        "When a limit is indeterminate because it goes to 0 divided by 0 or infinity divided by infinity, L'Hopital's rule can be used."
    ],
    "part2": [
        "L'Hopital's rule tells us that for a limit having indeterminate form of 0 divided by 0 or infinity divided by infinity, we can differentiate the numerator and denominator of the limit argument, independently, and the limit will remain unchanged.",
        "L'Hopital's rule tells us that we can independently differentiate the numerator and denominator of the limit argument without changing the result, if the limit has indeterminate form of 0 divided by 0 or infinity divided by infinity.",
        "According to L'Hopital's rule, the limit remains unchanged if we independently differentiate the numerator and denominator of the limit argument, provided the limit has indeterminate form of 0 divided by 0 or infinity divided by infinity."
    ],
    "part3": [
        "This is useful because differentiating the numerator and denominator often simplifies the limit and allows us to get a real number answer via substitution.",
        "Differentiating the numerator and denominator often causes the indeterminate limit to transform into a limit which yields a real number answer via substitution.",
        "After using L'Hopital's rule, the limit sometimes turns into one which can be solved via direct substitution."
    ]
}

###################
### HOOKE'S LAW ###
###################

hookes_law_template = ["{part1} {part2} {part3}"]
hookes_law_switches = {
    "part1": [
        "Hooke's law states that the force needed to extend or compress a spring by some distance is proportional to the distance.",
        "According to Hooke's law, the force needed to extend or compress a spring by some distance varies proportionally with the distance itself.",
        "Springs are governed by Hooke's law, which says that the force needed to extend or compress a spring by some distance is proportional to the distance.",
        "When extending or compressing a spring by some distance, Hooke's law applies. It states that that the force needed to extend or compress a spring by some distance is proportional to the distance."
    ],
    "part2": [
        "Consequently, the work needed to stretch or compress a spring from {eq}x_0{/eq} units past its normal length to {eq}x_1{/eq} units past its normal length is given by the integral {eq}W = \int_{x_0}^{x_1} kx dx{/eq}.",
        "Thus, the integral {eq}W = \int_{x_0}^{x_1} kx dx{/eq} gives the work needed to stretch or compress a spring from {eq}x_0{/eq} units past its normal length to {eq}x_1{/eq} units past its normal length.",
        "As such, stretching or compressing a spring from {eq}x_0{/eq} units past its normal length to {eq}x_1{/eq} units past its normal length requires an amount of work given by {eq}W = \int_{x_0}^{x_1} kx dx{/eq}.",
        "To stretch or compress a spring from {eq}x_0{/eq} units past its normal length to {eq}x_1{/eq} units past its normal length, then, one must input work equivalent to {eq}W = \int_{x_0}^{x_1} kx dx{/eq}."
    ],
    "part3": [
        "Solving the integral yields {eq}W = \frac{k}{2}(x_1^2 - x_0^2){/eq}.",
        "The integral is solved by {eq}W = \frac{k}{2}(x_1^2 - x_0^2){/eq}.",
        "Taking the antiderivative and evaluating at the bounds, the we reach {eq}W = \frac{k}{2}(x_1^2 - x_0^2){/eq}.",
        "Thus, {eq}W = \frac{k}{2}(x_1^2 - x_0^2){/eq}."
    ],
}

##################
### KINEMATICS ###
##################

kinematics_template = ["{part1} {part2}"]
kinematics_switches = {
    "part1": [
        "When an object is subject to constant acceleration, its trajectory follows the equations of kinematics, which can be manipulated using algebra.",
        "The laws of kinematics apply when an object is subject to constant acceleration.",
        "Finding trajectory of an object subject to constant acceleration involves only algebra.",
        "To find the trajectory of an object subject to a variable force, we need calculus. However, when the force is constant, all we need is algebra.",
        "An object subject to a constant force follows a quadratic trajectory."
    ],
    "part2": [
        "If the object has initial position {eq}r_0{/eq} and initial velocity {/eq}v_0{/eq} and is subject to a force causing constant acceleration {eq}a{/eq}, then after a time {eq}t{/eq} the function's position and velocity are given by\n{eq}r(t)=r_0+v_0t+\frac{a}{2}t^2{/eq}\n{eq}v(t)=v_0+at{/eq}",
        "After a time {eq}t{/eq} the function's position and velocity are given by\n{eq}r(t)=r_0+v_0t+\frac{a}{2}t^2{/eq}\n{eq}v(t)=v_0+at{/eq}\n where {eq}r_0{/eq} and {eq}v_0{/eq} are its initial position and velocity and {eq}a{/eq} is the constant acceleration.",
        "The function's position and velocity are given by\n{eq}r(t)=r_0+v_0t+\frac{a}{2}t^2{/eq}\n{eq}v(t)=v_0+at{/eq}\n after {eq}t{/eq} time steps, where {eq}r_0{/eq} and {eq}v_0{/eq} are its initial position and velocity and {eq}a{/eq} is the constant acceleration.",
        "If the function's initial position is given by {eq}r_0{/eq} and initial velocity is given by {/eq}v_0{/eq}, then after {eq}t{/eq} time steps, the function's position and velocity are given by \n{eq}r(t)=r_0+v_0t+\frac{a}{2}t^2{/eq}\n{eq}v(t)=v_0+at{/eq}"
    ]
}

############################
### LINEAR APPROXIMATION ###
############################

linear_approximation_template = ["{part1} {part2}"]
linear_approximation_switches = {
    "part1": [
        "Just as the tangent line is used for approximating single-variable functions, the tangent plane is used for approximating multivariable functions.",
        "In single-variable calculus, the tangent line is used for linear approximations. In mutivariable calculus, the tangent plane is used for linear approximations.",
        "The tangent plane is used for approximating multivariable functions, just like the tangent line is used for approximating single-variable functions.",
        "The tangent line and tangent plane are used for approximating single-variable and multivariable functions, respectively."
    ],
    "part2": [
        "Instead of {eq}\Delta f \\approx f'(x) \Delta x{/eq}, we have {eq}\Delta f \\approx \\nabla f(x,y,z) \cdot \langle \Delta x, \Delta y, \Delta z \\rangle{/eq}.",
        "For the tangent plane, we have {eq}\Delta f \\approx \\nabla f(x,y,z) \cdot \langle \Delta x, \Delta y, \Delta z \\rangle{/eq}, which can be remembered by its similarity to the tangent line approximation, {eq}\Delta f \\approx f'(x) \Delta x{/eq}.",
        "The tangent plane approximation is {eq}\Delta f \\approx \\nabla f(x,y,z) \cdot \langle \Delta x, \Delta y, \Delta z \\rangle{/eq}, and it is an extension of the tangent line approximation {eq}\Delta f \\approx f'(x) \Delta x{/eq}.",
        "In fact, the tangent line approximation {eq}\Delta f \\approx f'(x) \Delta x{/eq} is a special case of the tangent plane approximation {eq}\Delta f \\approx \\nabla f(x,y,z) \cdot \langle \Delta x, \Delta y, \Delta z \\rangle{/eq}.",
        "The tangent plane approximation is given by {eq}\Delta f \\approx \\nabla f(x,y,z) \cdot \langle \Delta x, \Delta y, \Delta z \\rangle{/eq}, and it generalizes the tangent line approximation {eq}\Delta f \\approx f'(x) \Delta x{/eq}."
    ]
}

##################
### ARC LENGTH ###
##################

arc_length_template = ["{part1} {part2} {part3}"]
arc_length_switches = {
    "part1": [
        "The formula for arc length differential can be found using the Pythagorean Theorem: {eq}ds = \sqrt{ dx^2 + dy^2 }{/eq}.",
        "Using the Pythagorean Theorem on differentials yields the arc length formula {eq}ds = \sqrt{ dx^2 + dy^2 }{/eq}.",
        "The arc length formula is {eq}ds = \sqrt{ dx^2 + dy^2 }{/eq} and can be seen as the Pythagoran Theorem applied to differentials",
        "The arc length formula, {eq}ds = \sqrt{ dx^2 + dy^2 }{/eq}, comes from the Pythagorean Theorem."
    ],
    "part2": [
        "To express the arc length differential in terms {eq}dx{/eq}, then, we can multiply by\n {eq}1 = \\frac{dx}{dx} = \\frac{dx}{\sqrt{dx^2} }{/eq} and then simplify: \n{eq}ds = \sqrt{ \\frac{dx^2}{dx^2} + \\frac{dy^2}{dx^2} }dx = \sqrt{ 1 + (\\frac{dy}{dx})^2 }dx{/eq}\n",
        "The arc length differential can also be expressed as\n {eq}ds = \sqrt{ \\frac{dx^2}{dx^2} + \\frac{dy^2}{dx^2} }dx = \sqrt{ 1 + (\\frac{dy}{dx})^2 }dx{/eq}\n",
        "When integrating, we usually use\n{eq}ds = \sqrt{ \\frac{dx^2}{dx^2} + \\frac{dy^2}{dx^2} }dx = \sqrt{ 1 + (\\frac{dy}{dx})^2 }dx{/eq}\n"
    ],
    "part3": [
        "We can also do this with differentials other than {eq}dx{/eq} -- for example, for parametrized functions, we have\n{eq}ds = \sqrt{ (\\frac{ds}{dt})^2 + (\\frac{dy}{dt})^2 }dt{/eq}.",
        "Likewise, for parametrized functions, we use\n{eq}ds = \sqrt{ (\\frac{ds}{dt})^2 + (\\frac{dy}{dt})^2 }dt{/eq}.",
        "For parametrized functions, the formula \n{eq}ds = \sqrt{ (\\frac{ds}{dt})^2 + (\\frac{dy}{dt})^2 }dt{/eq}\n is derived in a similar fashion."
    ]
}

###################################
### AVERAGE VALUE OF A FUNCTION ###
###################################

average_value_of_a_function_template = ["{part1} {part2} {part3}"]
average_value_of_a_function_switches = {
    "part1": [
        "In one dimension, the formula for average value of a function is given by {eq}\\frac{\int f(x) dx}{\int dx}{/eq}.",
        "The average value of a single-variable function is given by {eq}\\frac{\int f(x) dx}{\int dx}{/eq}.",
        "To find the average value of a single-variable function over an interval, one needs to sum the function and divide by the length of the integral: {eq}\\frac{\int f(x) dx}{\int dx}{/eq}.",
        "The average value of a single-variable function over an interval is computed by dividing the sum the function by the length of the interval: {eq}\\frac{\int f(x) dx}{\int dx}{/eq}.",
        "The average value of a single-variable function over an interval is computed as {eq}\\frac{\int f(x) dx}{\int dx}{/eq}, the sum dividing of the function divided by the length of the interval."
    ],
    "part2": [
        "In two dimensions, the average value of a function is given by {eq}\\frac{\int f(x,y) dxdy}{\int dxdy}{/eq}.",
        "The average value of a two-variable function is given by {eq}\\frac{\int f(x,y) dxdy}{\int dxdy}{/eq}.",
        "The average value of a function of two variables is given by {eq}\\frac{\int f(x,y) dxdy}{\int dxdy}{/eq}.",
        "To find the average value of a two-variable function over an area, one needs to sum the function and divide by the total area: {eq}\\frac{\int f(x,y) dxdy}{\int dxdy}{/eq}.",
        "The average value of a two-variable function over an area is computed by dividing the sum the function by the total area: {eq}\\frac{\int f(x,y) dxdy}{\int dxdy}{/eq}.",
        "The average value of a two-variable function over an interval is computed as {eq}\\frac{\int f(x,y) dxdy}{\int dxdy}{/eq}, the sum dividing of the function divided by the total area."
    ],
    "part3": [
        "In general, in ''n'' dimensions, the average value of a function is given by {eq}\\frac{\int f(x_1, ..., x_n) dx_1...dx_n}{\int dx_1...dx_n}{/eq}.",
        "The average value of an ''n''-variable function is given by {eq}\\frac{\int f(x_1, ..., x_n) dx_1...dx_n}{\int dx_1...dx_n}{/eq}.",
        "The average value of a function of ''n'' variables is given by {eq}\\frac{\int f(x_1, ..., x_n) dx_1...dx_n}{\int dx_1...dx_n}{/eq}.",
        "To find the average value of an ''n''-variable function over a volume, one needs to sum the function and divide by the total  volume: {eq}\\frac{\int f(x_1, ..., x_n) dx_1...dx_n}{\int dx_1...dx_n}{/eq}.",
        "The average value of an ''n''-variable function over an interval is computed by dividing the sum the function by the total volume: {eq}\\frac{\int f(x_1, ..., x_n) dx_1...dx_n}{\int dx_1...dx_n}{/eq}.",
        "The average value of an ''n''-variable function over an interval is computed as {eq}\\frac{\int f(x_1, ..., x_n) dx_1...dx_n}{\int dx_1...dx_n}{/eq}., the sum dividing of the function divided by the total volume."
    ]
}

######################
### TRIPLE PRODUCT ###
######################

triple_product_template = ["{part1} {part2} {part3}"]
triple_product_switches = {
    "part1": [
        "Given three edges of a parallelepiped, we can use the triple product formula to find the volume of the parallelepiped.",
        "The triple product formula can be used to find the volume of a parallelepiped, given its three edges.",
        "The volume of a parallelepiped can be found by applying the triple product formula to three of its edges."
    ],
    "part2": [
        "If the edge vectors are {eq}a,b,c{/eq}, then formula is given by {eq}(a \\times b) \cdot c{/eq}.",
        "If the edge vectors are {eq}u,v,w{/eq}, then formula is given by {eq}(u \\times v) \cdot w{/eq}.",
        "If the edge vectors are {eq}A,B,C{/eq}, then formula is given by {eq}(A \\times B) \cdot C{/eq}.",
        "The formula is given by {eq}(a \\times b) \cdot c{/eq}, where {eq}a,b,c{/eq} are the edge vectors.",
        "The formula is given by {eq}(u \\times v) \cdot w{/eq}, where {eq}u,v,w{/eq} are the edge vectors.",
        "The formula is given by {eq}(A \\times B) \cdot C{/eq}, where {eq}A,B,C{/eq} are the edge vectors."
    ],
    "part3": [
        "The formula works because the cross product gives a vector which is perpendicular to the base and has magnitude equal to the area of the base. Taking the dot product after the cross product, then, is equivalent to multiplying the area of the base by the height.",
        "To understand the formula, one can recall that the cross product gives a vector which is perpendicular to the base and whose length is the area of the base, so taking the dot product after the cross product multiplies the area of the base by the height.",
        "To intuit the formula, remember that the cross product gives a vector whose magnitude is equal to the area of the base and which is perpendicular to the base. The dot product, then, multiplies the area of the base by the height."
    ]
}

#########################
### INFLECTION POINTS ###
#########################

inflection_points_template = ["{part1} {part2} {part3}"]
inflection_points_switches = {
    "part1": [
        "An inflection point of a function is a point where the function changes concavity.",
        "A point where a function changes concavity is called an inflection point.",
        "If a function changes concavity at a point, then that point is called an inflection point.",
        "An inflection point of a function is a point where the function changes from concave down to concave up or from concave up to concave down.",
        "A point where a function changes from concave down to concave up or from concave up to concave down is called an inflection point.",
        "If a function changes concavity at a point, then that point is called an inflection point."
    ],
    "part2": [
        "Candidates for inflection points can be found by taking the second derivative of the function and setting it equal to zero. We also include those points where the second derivative is undefined.",
        "By setting the second derivative equal to zero, we can find candidates to inflection points. We also need to include those points where the second derivative is undefined.",
        "Just like we can find candidates for maxima and minima by setting the first derivative to zero, we can find candidates to inflection points by setting the second derivative to zero. We also include those points which make second derivative undefined.",
        "We can find candidates to inflection points by setting the second derivative to zero, just like we can find candidates for maxima and minima by setting the first derivative to zero. We also need to include those points which make second derivative undefined."
    ],
    "part3": [
        "However, one must check each of the candidates to make sure it is indeed an inflection point -- the function could, but does not necessarily, change concavity at these points.",
        "That being said, the function does not necessarily change concavity at these points, so we need to test them to be sure.",
        "However, just like points which make the first derivative zero could be saddle points and not optima, points which make the second derivative zero might not actually be inflection points. Therefore, we need to check each candidate to be sure.",
        "However, we need to test each candidate to be sure that it is an inflection point. Just like points which make the first derivative zero are not necessarily optima because they could be saddle points, points which make the second derivative zero are not necessarily inflection points."
    ]
}

######################
### PATH INTEGRALS ###
######################

path_integrals_template = ['{part1} {part2} {part3}']
path_integrals_switches = {
    'part1': [
        'Path integrals are integrals computed over one-dimensional curves that may be embedded in higher-dimensional space.',
        'Path integrals are one-dimensional integrals over curves that may be traced out in higher-dimensional space.'
    ],
    'part2': [
        'Along the path, it is easiest to parameterize the variables and write all of the variables and differentials in terms of the parameter.',
        'Along the path, then, it is possible to write the equation of the line in terms of a parameter and express the integrals in terms of that parameter.',
        'One can write the variables in terms of a parameter along the path, and take differentials in terms of the parameter too.',
        'The path can be expressed as a curve with a single parameter, so the integrals can written in terms of that parameter.'
    ],
    'part3': [
        'This way, the entire integral may be written in terms of the parameter, causing it to simplify to a single-variable integral.',
        'Writing everything in terms of the parameter will simplify the integral into a single-variable integral.',
        'The path integral can be transformed into a single-variable integral by expressing all of the terms with the same parameter.',
        'Then, the entire integral can be simplified into a single-variable integral by writing everything in terms of the parameter.',
        'Writing everything in terms of a single parameter, the path integral can be simplified into a single-variable integral.'
    ]
}

#######################
### CRITICAL POINTS ###
#######################

critical_points_template = ["{part1} {part2} {part3} {part4}"]
critical_points_switches = {
    "part1": [
        "At the maximum or minimum of a differentiable function, the derivative must be zero or undefined. Candidates for the maximum or minimum, i.e. those points which make the derivative zero or undefined, are called critical points.",
        "Candidates for the maximum or minimum of a function are called critical points. These are the points which make the derivative zero or undefined.",
        "The derivative must be zero or undefined at the maximum or minimum of a differentiable function. Therefore, we can find candidates for the maximum or minimum of a function by solving for those points which make the derivative zero or undefined. These points are called critical points.",
        "Critical points are those which make a function's derivative zero or undefined. Since the derivative must be zero or undefined at the maximum or minimum of a differentiable function, critical points are candidates for the maximum or minimum.",
        "Critical points are candidates for the maximum or minimum or minimum of a function. They are the points which make the derivative zero or undefined."
    ],
    "part2": [
        "However, critical points do not necessarily correspond to global optima of the function. A function may have many local optima, some of which may be more optimal than others.",
        "However, a function may have many local optima, some of which may be more optimal than others. Therefore, critical points do not necessarily correspond to global optima of the function.",
        "That being said, critical points do not necessarily correspond to global optima of the function, because some local optima my be more optimal than others.",
        "That being said, some local optima my be more optimal than others, so critical points do not necessarily correspond to global optima of the function."
    ],
    "part3": [
        "Furthermore, critical points need not even correspond to local optima of the function. They may represent saddle points, points where the function momentarily stops increasing or decreasing but then keeps on going in the same direction that it was originally going.",
        "But critical points need not even correspond to local optima of the function -- they may represent saddle points where the function momentarily stops increasing or decreasing but then continues in the same direction.",
        "Critical points need not even correspond to local optima of the function, though. For example, the derivative is also zero at saddle points, where the function momentarily stops increasing or decreasing but then continues in the same direction."
    ],
    "part4": [
    "Thus, to find the optima of a function, we need to evaluate the function at each of the critical points and then compare the resulting values.",
    "Thus, we must evaluate the function at each of the critical points and then compare the resulting values in order to find the optima of the function.",
    "Thus, optimizing a function requires us to evaluate the function at each of the critical points and then compare the resulting values."
    ]
}

###############################
### APPROXIMATING INTEGRALS ###
###############################

approximating_integrals_template = ["{part1} {part2} {part3}"]
approximating_integrals_switches = {
    "part1": [
        "Integrals can be numerically computed by partitioning the domain of integration into smaller pieces, evaluating the integrand somewhere on each of those pieces, and then adding each piece's contribution to the integral.",
        "Integrals can be numerically approximated by splitting the domain of integration into smaller pieces, evaluating the integrand somewhere on each of those pieces, and then summing each piece's contribution to the integral.",
        "To approximate an integral, we can split the domain of integration into smaller pieces and sum up the area or volume over all of those pieces.",
        "To numerically commpute an integral, we can split the domain of integration into smaller pieces and sum up the area or volume over all of those pieces.",
        "To numerically commpute an integral, we can partition the domain of integration into smaller pieces and add up the area or volume over all of those pieces.",
        "Integrals can be approximating by partitioning them into smaller pieces, calculating the area or volume for each piece, and adding up the area or volume of all of the pieces."
    ],
    "part2": [
        "The most basic estimation methods include left and right Riemann sums, which involve computing the integral as the sum of areas of equal-width rectangles whose height to the left or right corner is given by the function value.",
        "The most basic estimation methods include left and right Riemann sums, which split the integral into rectangles of equal width, each of whose height to the the left or right corner is given by the function value.",
        "Riemann sums, for example, involve computing the integral as the sum of areas of equal-width rectangles whose height to the left or right corner is given by the function value.",
        "Riemann sums, for example, involve splitting the integral into rectangles of equal width, each of whose height to the the left or right corner is given by the function value."
    ],
    "part3": [
        "More advanced estimation methods include midpoint approximation, where the height midway between the left and right corners is given by the function value, and trapezoidal approximation, which takes an average of the left and right Riemann sums, and trapezoidal approximation.",
        "Midpoint approximation is a more advanced method where the height midway between the left and right corners is given by the function value; so is trapezoidal approximation, which takes an average of the left and right Riemann sums, and trapezoidal approximation.",
        "There are more advanced methods which yield better approximates, such as midpoint and trapezoidal approximation. In midpoint approximation, the height midway between the left and right corners is given by the function value; in trapezoidal approximation, the left and right Riemann sums are averaged."
    ]
}

#####################
### QUOTIENT RULE ###
#####################

quotient_rule_template = ["{part1} {part2}"]
quotient_rule_switches = {
    "part1": [
        "The quotient rule can be used to find derivatives of rational functions. It is given by: {eq}\left( \\frac{f(x)}{g(x)} \\right)' = \\frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}{/eq}.",
        "To find derivatives of rational functions, we use the quotient rule, which is given by {eq}\left( \\frac{f(x)}{g(x)} \\right)' = \\frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}{/eq}.",
        "Find the derivative of a rational function involves the use the quotient rule, which is given by {eq}\left( \\frac{f(x)}{g(x)} \\right)' = \\frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}{/eq}.",
        "The quotient rule is given by {eq}\left( \\frac{f(x)}{g(x)} \\right)' = \\frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}{/eq}. It is used to find derivatives of rational functions."
    ],
    "part2": [
        "However, using the product rule can be time-consuming, so one should be sure to simplify a rational expression first, before using the product rule.",
        "The product rule can be computationally-intensive, so one should be sure to simplify a rational expression as much as possible before using it.",
        "Before using the product rule, though, one should be sure to simplify a rational expression as much as possible. This will ensure that no unnecessary computations are performed.",
        "Before using the product rule, one should be sure to simplify a rational expression as much as possible, so as to reduce the amount of time and effort that is expended through the computation."
    ]
}

####################
### PRODUCT RULE ###
####################

product_rule_template = ["{part1} {part2}"]
product_rule_switches = {
    "part1": [
        "The product rule is used for taking the derivative of the product of two functions. According to the product rule, the derivative of the product {eq}f(x)g(x){/eq} is given by {eq}f'(x)g(x) + f(x)g'(x){/eq}.",
        "To take the derivative of the product of two functions, we use the product rule, which is given by {eq}(f(x)g(x))'= f'(x)g(x) + f(x)g'(x){/eq}.",
        "The product rule, given by {eq}(f(x)g(x))'= f'(x)g(x) + f(x)g'(x){/eq}, is used to take the derivative of the product of functions.",
        "When we want to take the derivative of two functions which are multiplied together, we can use the product rule, which is given by {eq}(f(x)g(x))'= f'(x)g(x) + f(x)g'(x){/eq}.",
        "The product rule is given by {eq}(f(x)g(x))'= f'(x)g(x) + f(x)g'(x){/eq}. It is used when we want to take the derivative of the product of functions, i.e. functions which are multiplied together."
    ],
    "part2": [
        "For the product of more than two functions, the product rule follows the same format. For example, {eq}(f(x)g(x)h(x))'= f'(x)g(x)h(x) + f(x)g'(x)h(x) + f(x)g(x)h'(x){/eq}. It also works with the dot product for vector functions.",
        "The product rule also works for products of more than two functions, e.g. {eq}(f(x)g(x)h(x))'= f'(x)g(x)h(x) + f(x)g'(x)h(x) + f(x)g(x)h'(x){/eq}. It also works with the dot product for vector functions.",
        "In general, for a product of more than two functions, the product rule involves taking the derivative of each function and mutliplying it by the other functions, and then adding up all the terms. For example, {eq}(f(x)g(x)h(x))'= f'(x)g(x)h(x) + f(x)g'(x)h(x) + f(x)g(x)h'(x){/eq}. It also works with the dot product for vector functions.",
        "For products of more than two functions, the product rule is similar: {eq}(f(x)g(x)h(x))'= f'(x)g(x)h(x) + f(x)g'(x)h(x) + f(x)g(x)h'(x){/eq}. It also works with the dot product for vector functions."
    ]
}

#########################
### POLAR COORDINATES ###
#########################

polar_coordinates_template = ["{part1} {part2}"]
polar_coordinates_switches = {
    "part1": [
        "Polar coordinates can be used to exploit circular symmetry, while Cartesian coordinates can be used to exploit rectangular symmetry.",
        "To take advantage of circular symmetry, we use polar coordinates; to take advantage of rectangular symmetry, we use Cartesian coordinates.",
        "To take advantage of rectangular symmetry, we use Cartesian coordinates; to take advantage of circular symmetry, we use polar coordinates.",
        "Cartesian coordinates are used to exploit rectangular symmetry, and polar coordinates are used to exploit circular symmetry.",
        "Cartesian and polar coordinates are used to take advantage of rectangular and circular symmetry, respectively.",
        "Polar and Cartesian coordinates are used to take advantage of circular and rectangular symmetry, respectively."
    ],
    "part2": [
        "Converting from Cartesian coordinates to polar coordinates is accomplished by assigning {eq}r = \\sqrt{x^2 + y^2}{/eq} and {eq}\\theta = \\arctan \\frac{y}{x}{/eq}. Conversely, converting from polar coordinates to Cartesian coordinates is accomplished through {eq}x=r\cos \\theta{/eq} and {eq}y = r\\sin \\theta{/eq}.",
        "Converting from polar coordinates to Cartesian coordinates is accomplished through {eq}x=r\cos \\theta{/eq} and {eq}y = r\\sin \\theta{/eq}. Conversely, converting from Cartesian coordinates to polar coordinates is accomplished by assigning {eq}r = \\sqrt{x^2 + y^2}{/eq} and {eq}\\theta = \\arctan \\frac{y}{x}{/eq}.",
        "To convert from Cartesian coordinates to polar coordinates, we use the transformation {eq}r = \\sqrt{x^2 + y^2}{/eq} and {eq}\\theta = \\arctan \\frac{y}{x}{/eq}; to convert from polar coordinates to Cartesian coordinates, we use the transformation {eq}x=r\cos \\theta{/eq} and {eq}y = r\\sin \\theta{/eq}.",
        "To convert from polar coordinates to Cartesian coordinates, we use the transformation {eq}x=r\cos \\theta{/eq} and {eq}y = r\\sin \\theta{/eq}; to convert from Cartesian coordinates to polar coordinates, we use the transformation {eq}r = \\sqrt{x^2 + y^2}{/eq} and {eq}\\theta = \\arctan \\frac{y}{x}{/eq}.",
        "The change of variables {eq}r = \\sqrt{x^2 + y^2}{/eq} and {eq}\\theta = \\arctan \\frac{y}{x}{/eq} is used to convert from Cartesian coordinates to polar coordinates. Likewise, the change of variables {eq}x=r\cos \\theta{/eq} and {eq}y = r\\sin \\theta{/eq} is used to convert from polar coordinates to Cartesian coordinates.",
        "The change of variables {eq}x=r\cos \\theta{/eq} and {eq}y = r\\sin \\theta{/eq} is used to convert from polar coordinates to Cartesian coordinates. Likewise, the change of variables {eq}r = \\sqrt{x^2 + y^2}{/eq} and {eq}\\theta = \\arctan \\frac{y}{x}{/eq} is used to convert from Cartesian coordinates to polar coordinates."
    ]
}

###########################################
### THE FUNDAMENTAL THEOREM OF CALCULUS ###
###########################################

the_fundamental_theorem_of_calculus_template = ["{part1} {part2}"]
the_fundamental_theorem_of_calculus_switches = {
    "part1": [
        "Part 1 of the Fundamental Theorem of Calculus states that for an integral function {eq}F(x) = \int_{x_0}^x f(t)dt{/eq}, the derivative is given by {eq}F'(x) = f(x){/eq}."
    ],
    "part2": [
        "Intuitively, {eq}F(x){/eq} measures the amount of area of {eq}f(t){/eq} from {eq}t=x_0{/eq} to {eq}t=x{/eq}, and the amount of change at {eq}t=x{/eq} is the amount of area introduced at {eq}t=x{/eq}, which is given by {eq}f(x){/eq}."
    ]
}

#################################################
### EVALUATING LIMITS VIA DIRECT SUBSTITUTION ###
#################################################

evaluating_limits_via_direct_substitition_template = ["{part1} {part2}"]
evaluating_limits_via_direct_substitition_switches = {
    "part1": [
        "When possible, the simplest way to evaluate a limit of the function is to simply plug the limit directly into the function. This technique is called the method of direct substitution, and works whenever the function is continuous.",
        "The simplest way to evaluate a limit of the function is the method of direct substitution, which involves substituting the limit directly into the function. This technique works whenever the function is continuous.",
        "When possible, we can evaluate limits by substituting the limit directly into the function. This is called the method of direct substitution, and it works whenever the function is continuous.",
        "The method of direct substutition involves calculating limits by substituting them directly into the function. This method works whenever the function is continuous.",
        "Whenever a function is continuous, the method of direct substutition may be used. This technique involves calculating limits by substituting them directly into the function."
    ],
    "part2": [
        "Sometimes, even though direct substitution may not be possible initially, it is possible to simplify the argument of the limit so that the method of direct substitution can be used.",
        "Even at times when direct substitution may not be possible initially, it may turn out to be possible after simplifying the argument of the limit.",
        "Sometimes, discontinuous functions can be converted to continuous functions via simplifying. Therefore, one's first approach to solving limits should be to simplify the argument and check if direct substitution is possible.",
        "One's first approach to evaluating a limit should be to simplify the argument and check if direct substitution is possible, because discontinuous functions can sometimes be converted to continuous functions via simplifying."
    ]
}

############################################
### ACCELERATION, VELOCITY, AND POSITION ###
############################################

acceleration_velocity_position_template = ["{part1} {part2}"]
acceleration_velocity_position_switches = {
    "part1": [
        "When working with acceleration, velocity, and position, it is vital to know that velocity is the derivative of position, and acceleration is the derivative of velocity."
    ],
    "part2": [
        "Thus, one can find velocity by integrating acceleration, and one can find position by integrating velocity."
    ]
}

#################################
### CHARACTERISTIC POLYNOMIAL ###
#################################

characteristic_polynomial_template = ["{part1} {part2} {part3}"]
characteristic_polynomial_switches = {
    "part1": [
        "For a differential equation {eq}ay' ' + by' + cy = 0{/eq}, the characteristic polynomial is given by {eq}ar^2 + br + c = 0{/eq}."
    ],
    "part2": [
        "If the roots {eq}r_1, r_2{/eq} of the polynomial are distinct, the solutions are given by the real and imaginary parts of {eq}c_1e^{r_1x} + c_2e^{r_2x}{/eq}."
    ],
    "part3": [
        "If the roots {eq}r_1=r_2 = r{/eq} are repeated, then the solutions are given by the real and imaginary parts of {eq}c_1e^{rx} + c_2xe^{rx}{/eq}."
    ]
}

##############################################
### DERIVATIVE OF THE EXPONENTIAL FUNCTION ###
##############################################

derivative_of_exponential_template = ["{part1} {part2} {part3}"]
derivative_of_exponential_switches = {
    "part1": [
        "The exponential function is given by {eq}e^x{/eq}, where {eq}e \\approx 2.71{/eq} is Euler's constant. It is the function with the special property that its derivative is itself."
    ],
    "part2": [
        "That is to say, if {eq}f(x) = e^x{/eq}, then {eq}f'(x) = e^x{/eq}, and thus {eq}f^{(n)}(x) = e^x{/eq} for every ''n''th derivative."
    ],
    "part3": [
        "We sometimes also encounter exponential functions of the form {eq}e^{rx}{/eq} for a constant {eq}r{/eq}. If {eq}f(x) = e^{rx}{/eq}, then by the chain rule we have {eq}f'(x) = re^{rx}{/eq}, and thus {eq}f^{(n)}(x) = r^ne^{rx}{/eq} for every ''n''th derivative."
    ]
}

####################################
### EXPONENTIAL GROWTH AND DECAY ###
####################################

exponential_growth_and_decay_template = ["{part1} {part2} {part3}"]
exponential_growth_and_decay_switches = {
    "part1": [
   
    ],
    "part2": [
      
    ],
    "part3": [
        
    ]
}



###############

import random

def make_contexts():
    
    contexts={}
    
    # randomized
    contexts['!!!Cross Product'] = {'template': cross_product_template, 'switches': cross_product_switches}
    contexts['!!!Line Integrals'] = {'template': line_integrals_template, 'switches': line_integrals_switches}
    contexts['!!!Lagrange Multipliers'] = {'template': lagrange_multipliers_template, 'switches': lagrange_multipliers_switches}
    contexts['!!!Separable Differential Equations'] = {'template': separable_differential_equations_template, 'switches': separable_differential_equations_switches}
    contexts['!!!Dot Product'] = {'template': dot_product_template, 'switches': dot_product_switches}

    contexts['!!!Initial Condition Problems'] = {'template': initial_condition_problems_template, 'switches': initial_condition_problems_switches}
    contexts['!!!Equation of a Sphere'] = {'template': equation_of_a_sphere_template, 'switches': equation_of_a_sphere_switches}
    contexts['!!!Directional Derivatives'] = {'template': directional_derivatives_template, 'switches': directional_derivatives_switches}
    contexts['!!!Indefinite Integrals'] = {'template': indefinite_integrals_template, 'switches': indefinite_integrals_switches}
    contexts['!!!Tangent Lines'] = {'template': tangent_lines_template, 'switches': tangent_lines_switches}

    contexts['!!!Derivative as Rate of Change'] = {'template': derivative_as_rate_of_change_template, 'switches': derivative_as_rate_of_change_switches}
    contexts['!!!Tangent Planes'] = {'template': tangent_planes_template, 'switches': tangent_planes_switches}
    contexts["!!!L'Hopital's Rule"] = {'template': lhopitals_rule_template, 'switches': lhopitals_rule_switches}
    contexts["!!!Hooke's Law"] = {'template': hookes_law_template, 'switches': hookes_law_switches}
    contexts["!!!Kinematics"] = {'template': kinematics_template, 'switches': kinematics_switches}

    contexts["!!!Linear Approximation"] = {'template': linear_approximation_template, 'switches': linear_approximation_switches}
    contexts["!!!Arc Length"] = {'template': arc_length_template, 'switches': arc_length_switches}
    contexts["!!!Average Value of a Function"] = {'template': average_value_of_a_function_template, 'switches': average_value_of_a_function_switches}
    contexts["!!!Triple Product"] = {'template': triple_product_template, 'switches': triple_product_switches}
    contexts["!!!Inflection Points"] = {'template': inflection_points_template, 'switches': inflection_points_switches}
    
    contexts["!!!Path Integrals"] = {'template': path_integrals_template, 'switches': path_integrals_switches}
    contexts["!!!Optimizing via Critical Points"] = {'template': critical_points_template, 'switches': critical_points_switches}
    contexts["!!!Approximating Integrals"] = {'template': approximating_integrals_template, 'switches': approximating_integrals_switches}
    contexts["!!!Quotient Rule"] = {'template': quotient_rule_template, 'switches': quotient_rule_switches}
    contexts["!!!Product Rule"] = {'template': product_rule_template, 'switches': product_rule_switches}
    
    contexts["!!!Polar Coordinates"] = {'template': polar_coordinates_template, 'switches': polar_coordinates_switches}
    
    # not randomized
    contexts["!!!The Fundamental Theorem of Calculus"] = {'template': the_fundamental_theorem_of_calculus_template, 'switches': the_fundamental_theorem_of_calculus_switches}
    contexts["!!!Evaluating Limits via Direct Substitution"] = {'template': evaluating_limits_via_direct_substitition_template, 'switches': evaluating_limits_via_direct_substitition_switches}
    contexts["!!!Acceleration, Velocity, and Position"] = {'template': acceleration_velocity_position_template, 'switches': acceleration_velocity_position_switches}
    contexts["!!!The Characteristic Polynomial"] = {'template': characteristic_polynomial_template, 'switches': characteristic_polynomial_switches}
    contexts["!!!Derivative of the Exponential Function"] = {'template': derivative_of_exponential_template, 'switches': derivative_of_exponential_switches}



    
    return contexts

def make_random_context(lookup="!!!Dot Product"):
    
    contexts = make_contexts()

    template = contexts[lookup]['template']
    switches = contexts[lookup]['switches']
    switches_instance = {k:random.choice(v) for k,v in switches.iteritems()}
    template_instance = random.choice(template).format(**switches_instance)

    template_instance = template_instance.replace('  ',' ')

    print lookup+'\n'+template_instance
    
def print_lookups():
    contexts = make_contexts()
    print contexts.keys()
