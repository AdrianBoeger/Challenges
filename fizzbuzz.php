<?php

for ($i; $i<=101; $i++)
{
    if ($i % 15 == 0)
    {
        echo 'Fizzbuzz';
    }
    elseif ($i % 3 == 0)
    {
        echo 'Fizz';
    }
    elseif ($i % 5 == 0)
    {
        echo 'Buzz';
    }
    else {
        echo $i;
    }
}
