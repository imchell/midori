start_skaffold = "skaffold start"
end_skaffold = "skaffold delete"
list_pods = "kubectl get pods --all-namespaces"
list_files_inside_pod = "kubectl exec -it loadgenerator-xxx -c main ls"
copy_file_from_pod = "kubectl cp default/loadgenerator-xxx:/loadgen/result_stats.csv ~/research/result_stats.csv"