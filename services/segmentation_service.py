from sklearn.cluster import KMeans
import numpy as np

# initialize model (simple version for now)
kmeans = KMeans(n_clusters=4, random_state=42)

def segment_user(features):
    X = np.array(list(features.values())).reshape(1, -1)

    # temporary fit (will improve later)
    cluster = kmeans.fit_predict(X)[0]

    mapping = {
        0: "power_user",
        1: "declining_user",
        2: "new_user",
        3: "dormant_user"
    }

    return mapping.get(cluster, "unknown")