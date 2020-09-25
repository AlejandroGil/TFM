#!/bin/bash
while :
do
  echo {\"value\":$(((RANDOM % 100)  + 1 ))} | kafkacat -b $1 -t $2
  sleep 1
done
