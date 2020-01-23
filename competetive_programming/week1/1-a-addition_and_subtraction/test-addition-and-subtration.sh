
X=1
Y=1
Z=1
i=0


until [ $X -gt 1000 ]
do
    Y=1
    Z=1
    # Loop Y
    until [ $Y -gt 1000 ]
    do
        # Loop X
        Z=1
        until [ $Z -gt 1000 ]
        do
            # Loop Z
            echo "Test [$i] X=$X Y=$Y Z=$Z \t\t - OK"
            echo "$X $Y $Z \n" > sample.in
            
            # solution
            ./addition-and-subtraction < sample.in > out
            # trivial
            python3 addition-and-subtraction.py < sample.in > out_trivial
            # Check ans
            diff out out_trivial >/dev/null
            
            if [ $? -ne '0' ] ; then
                echo "Error on test"
                return 13
            fi
            
            Z=$((Z+65))
            i=$((i+1))
        done
        Y=$((Y+65))
    done
    
    X=$((X+65))
done
echo " -- ALL $i TEST OK -- "


