#!/bin/bash
kops edit ig nodes
kops edit ig master-eu-west-1a
kops update cluster --yes
kops rolling-update cluster