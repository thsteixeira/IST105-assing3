<!DOCTYPE html>
<html>
<head>
    <title>Calculation with Python</title>
</head>
<body>
    <h1>Enter three numbers in the URL to calculate</h1>
    <p>Use the URL format: <strong>index.php?x=2&y=3&z=4</strong></p>

    <?php
    if (isset($_GET["x"]) && isset($_GET["y"]) && isset($_GET["z"])) {
        $a = $_GET["x"];
        $b = $_GET["y"];
        $c = $_GET["z"];
        $output = shell_exec("python3 calculate.py " . escapeshellarg($x) . " " . escapeshellarg($y) . " " . escapeshellarg($z));
        echo "<h2>The calculation result is: $output</h2>";
    } else {
        echo "<h2>Please provide three numbers in the URL.</h2>";
    }
    ?>
</body>
</html>