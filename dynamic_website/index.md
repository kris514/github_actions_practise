#This is my own index where I will test the appearance of png images

<html lang="en">
<head>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.min.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/handlebars@latest/dist/handlebars.js"></script>
  
  <script src="PageManager.js"></script>
  <script src="GraphTileManager.js"></script>
  <script type="text/javascript" src="depth_data.json"></script>
  <script type="text/javascript" src="depth_line_data.json"></script>
  <script type="text/javascript" src="time_data.json"></script>
  <script type="text/javascript" src="time_line_data.json"></script>
  <link href="style.css" rel="stylesheet"></link>

</head>
<body>

## Software Benchmarking

Please select the combination of circuit, compiler, and architecture that you
would like to view by clicking on "Toggle Options" beneath each plot. 
Properties of these parameters are defined below. Data is not available for
each combination, and these options are greyed out accordingly. Please hover 
over the legend to display equations for lines of best fit.

<div id="graph-tile-container"></div>

The complete dataset used to create these plots
can be retrieved from Dan.

<script>
  $(function(){
    var includes = $('[data-include]');
    jQuery.each(includes, function(){
      var file = $(this).data('include') + '.html';
      $(this).load(file);
    });
  });
</script>

### Compiler Passes

Here we present results from software benchmarking. When optimising take place,
the compilation strategy used are the "most optimised general purpose"
strategies which are default in each software package. When the compilers are
non-optimising, the routing method is being tested. In particular:

- optimising pytket:
  [FullPeepholeOptimise](https://cqcl.github.io/pytket/build/html/passes.html#pytket.passes.FullPeepholeOptimise)
- non-optimising pytket:
  [DefaultMappingPass](https://cqcl.github.io/pytket/build/html/passes.html?highlight=default%20mapping%20pass#pytket.passes.DefaultMappingPass)
- pytket chemistry:
  [PauliSimp](https://cqcl.github.io/pytket/build/html/passes.html#pytket.passes.GuidedPauliSimp) 
  followed by
  [FullPeepholeOptimise](https://cqcl.github.io/pytket/build/html/passes.html#pytket.passes.FullPeepholeOptimise)
- optimising qiskit:
  [level_3_pass_manager](https://qiskit.org/documentation/stubs/qiskit.transpiler.preset_passmanagers.level_3_pass_manager.html#qiskit.transpiler.preset_passmanagers.level_3_pass_manager)
- non-optimising qiskit:
  [level_0_pass_manager](https://qiskit.org/documentation/stubs/qiskit.transpiler.preset_passmanagers.level_0_pass_manager.html#qiskit.transpiler.preset_passmanagers.level_0_pass_manager) 
- quil:
  [QVMCompiler](https://pyquil-docs.rigetti.com/en/stable/apidocs/autogen/pyquil.api.QVMCompiler.html?highlight=QVMCompiler#pyquil.api.QVMCompiler) 

### Circuit Classes

The circuits included are the following:

- **known optimal**: These relate to the circuits discussed in [this
  paper](https://arxiv.org/abs/2002.09783). The circuits from that paper have
  been altered so that the `backbone' consists only of CZ gates, as opposed to
  a mixture of 1 and 2 qubit gates. This is because 2 qubit gates are the
  greatest source of errors. These circuit test routing, and so no optimisation
  should be performed on these circuits.
- **square**: These are the *square circuits* as defined in [this paper][1].
  They are similar to [quantum volume](https://arxiv.org/abs/1811.12926) used
  for device benchmarking, and to random circuits used for demonstrations of
  quantum computational supremacy.
- **shallow**: These are the "shallow circuits" as defined in [this paper][1].
  They are random IQP circuits with initial connectivity defined by a random
  graph of degree at most 3.
- **deep**: These are the *deep circuits* as defined in [this paper][1]. They
  are built from repeated UCCSD ansatz circuits, up to a depth sufficient to
  produce output probabilities which are exponentially distributed.
- **qaoa**: These circuits are inspired by qaoa applied to maxcut on random
  3-regular graphs, as discussed in [this
  paper](https://arxiv.org/abs/2004.04197). Here parameters are set at random,
  and depth 2 qaoa is implemented. An insightful video can be found
  [here](https://youtu.be/bhNin0MjH9I).
- **basis rotation**: Random Givens rotations based basis rotations, inspired
  by [this work](https://arxiv.org/abs/2004.04174). This is an important
  subroutine in many quantum chemistry calculations. An insightful video can be
  found [here](https://youtu.be/nfXEdbPXGek).

[1]: https://arxiv.org/abs/2006.01273 "Application motivated benchmarking"

The circuits used can be found in [this
repository](https://github.com/CQCL-DEV/software_benchmarking), with all of
them being run in this case.

## Improvements ans Usage

<mark>We welcome feedback on these results and their presentation</mark>. 
Comments should be directed to Dan Mills. In particular we aim for this suite 
to facilitate development of tket, and so aim
for the results to present information that is useful in this regard. If some
other set of statistics, or other presentation there of, is of value then
please let us know.

We will attempt to keep these results up to date, although you may wish to
contact Dan to verify this before using the results for some other purpose,
such as presentations

</body>
</html>



![Test Image 4](https://github.com/kris514/github_actions_practise/blob/main/images/google%20arch.png, 'Google Arch')

![Test Image 5](https://github.com/kris514/github_actions_practise/blob/main/images/ibmq_toronto.png)
