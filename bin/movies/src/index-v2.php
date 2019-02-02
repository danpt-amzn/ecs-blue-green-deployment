<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>ECS Microservice Demo App</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="assets/css/bootstrap.min.css" rel="stylesheet">
        <style>body {margin-top: 40px; background-color: #0EF318;}</style>
        <link href="assets/css/bootstrap-responsive.min.css" rel="stylesheet">
        <!--[if lt IE 9]><script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
    </head>

    <body>
        <div class="container">
            <div class="hero-unit">
                <h1>ECS Microservice Demo App</h1>
                <h2>Welcome</h2>
                <p>Web App running on a container in Amazon ECS.</p>
                <p>Container PHP version <?php echo phpversion(); ?>.</p>
                 <?php
                       $url = 'http://192.168.1.108:5000/Query?year=2000'; // path to your JSON file
                       $json = file_get_contents($url);
                       $koyim=  json_decode($json, true);
                       echo "<br>";
                    foreach($koyim['Items'] as $key) {
                       echo $key['title'];
                       echo "<br>";
                       echo $key['info']['plot'];
                       echo "<br>"; 
                       echo $key['year'];
                       echo "<br>";
                       echo $key['info']['actors'][0];
                       $image = $key['info']['image_url'];
                       echo '<img src="';
                       echo $image;
                       echo '">';
                       echo "<br>";
                     }
?>
            </div>
        </div>

        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>
        <script src="assets/js/bootstrap.min.js"></script>
    </body>

</html>
