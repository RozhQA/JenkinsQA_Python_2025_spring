class XmlConfigs:
    FREESTYLE_PROJECT = """<project>
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>false</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <builders/>
  <publishers/>
  <buildWrappers/>
</project>"""

    PIPELINE = """<flow-definition plugin="workflow-job@1508.v9cb_c3a_a_89dfd">
  <keepDependencies>false</keepDependencies>
  <properties/>
  <triggers/>
  <disabled>false</disabled>
</flow-definition>"""

    MULTI_CONFIGURATION_PROJECT = """<matrix-project plugin="matrix-project@847.v88a_f90ff9f20">
  <keepDependencies>false</keepDependencies>
  <properties/>
  <scm class="hudson.scm.NullSCM"/>
  <canRoam>false</canRoam>
  <disabled>false</disabled>
  <blockBuildWhenDownstreamBuilding>false</blockBuildWhenDownstreamBuilding>
  <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
  <triggers/>
  <concurrentBuild>false</concurrentBuild>
  <axes/>
  <builders/>
  <publishers/>
  <buildWrappers/>
  <executionStrategy class="hudson.matrix.DefaultMatrixExecutionStrategyImpl">
    <runSequentially>false</runSequentially>
  </executionStrategy>
</matrix-project>"""

    FOLDER = """<com.cloudbees.hudson.plugins.folder.Folder plugin="cloudbees-folder@6.999.v42253c105443">
  <properties/>
  <folderViews class="com.cloudbees.hudson.plugins.folder.views.DefaultFolderViewHolder">
    <views>
      <hudson.model.AllView>
        <owner class="com.cloudbees.hudson.plugins.folder.Folder" reference="../../../.."/>
        <name>All</name>
        <filterExecutors>false</filterExecutors>
        <filterQueue>false</filterQueue>
        <properties class="hudson.model.View$PropertyList"/>
      </hudson.model.AllView>
    </views>
    <tabBar class="hudson.views.DefaultViewsTabBar"/>
  </folderViews>
  <healthMetrics/>
  <icon class="com.cloudbees.hudson.plugins.folder.icons.StockFolderIcon"/>
</com.cloudbees.hudson.plugins.folder.Folder>"""

    MULTIBRANCH_PIPELINE = """<org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject plugin="workflow-multibranch@803.v08103b_87c280">
  <properties/>
  <folderViews class="jenkins.branch.MultiBranchProjectViewHolder" plugin="branch-api@2.1214.v3f652804588d">
    <owner class="org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject" reference="../.."/>
  </folderViews>
  <healthMetrics/>
  <icon class="jenkins.branch.MetadataActionFolderIcon" plugin="branch-api@2.1214.v3f652804588d">
    <owner class="org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject" reference="../.."/>
  </icon>
  <orphanedItemStrategy class="com.cloudbees.hudson.plugins.folder.computed.DefaultOrphanedItemStrategy" plugin="cloudbees-folder@6.999.v42253c105443">
    <pruneDeadBranches>true</pruneDeadBranches>
    <daysToKeep>-1</daysToKeep>
    <numToKeep>-1</numToKeep>
    <abortBuilds>false</abortBuilds>
  </orphanedItemStrategy>
  <triggers/>
  <disabled>false</disabled>
  <sources class="jenkins.branch.MultiBranchProject$BranchSourceList" plugin="branch-api@2.1214.v3f652804588d">
    <data/>
    <owner class="org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject" reference="../.."/>
  </sources>
  <factory class="org.jenkinsci.plugins.workflow.multibranch.WorkflowBranchProjectFactory">
    <owner class="org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject" reference="../.."/>
    <scriptPath>Jenkinsfile</scriptPath>
  </factory>
</org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject>"""

    ORGANIZATION_FOLDER = """<jenkins.branch.OrganizationFolder plugin="branch-api@2.1214.v3f652804588d">
  <properties>
    <jenkins.branch.OrganizationChildTriggersProperty>
      <templates>
        <com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger plugin="cloudbees-folder@6.999.v42253c105443">
          <spec>H H/4 * * *</spec>
          <interval>86400000</interval>
        </com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger>
      </templates>
    </jenkins.branch.OrganizationChildTriggersProperty>
    <jenkins.branch.OrganizationChildOrphanedItemsProperty>
      <strategy class="jenkins.branch.OrganizationChildOrphanedItemsProperty$Inherit"/>
    </jenkins.branch.OrganizationChildOrphanedItemsProperty>
  </properties>
  <folderViews class="jenkins.branch.OrganizationFolderViewHolder">
    <owner reference="../.."/>
  </folderViews>
  <healthMetrics/>
  <icon class="jenkins.branch.MetadataActionFolderIcon">
    <owner class="jenkins.branch.OrganizationFolder" reference="../.."/>
  </icon>
  <orphanedItemStrategy class="com.cloudbees.hudson.plugins.folder.computed.DefaultOrphanedItemStrategy" plugin="cloudbees-folder@6.999.v42253c105443">
    <pruneDeadBranches>true</pruneDeadBranches>
    <daysToKeep>-1</daysToKeep>
    <numToKeep>-1</numToKeep>
    <abortBuilds>false</abortBuilds>
  </orphanedItemStrategy>
  <triggers>
    <com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger plugin="cloudbees-folder@6.999.v42253c105443">
      <spec>H H/4 * * *</spec>
      <interval>86400000</interval>
    </com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger>
  </triggers>
  <disabled>false</disabled>
  <navigators/>
  <projectFactories>
    <org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProjectFactory plugin="workflow-multibranch@803.v08103b_87c280">
      <scriptPath>Jenkinsfile</scriptPath>
    </org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProjectFactory>
  </projectFactories>
  <buildStrategies/>
</jenkins.branch.OrganizationFolder>"""


class DashboardTable:
    HEADERS_MAP = {
        "Status of the last build": "S",
        "Weather report": "W",
        "Name": "Name",
        "Last Success": "Last Success",
        "Last Failure": "Last Failure",
        "Last Duration": "Last Duration",
        "Schedule": ""
    }

    PROJECT_NAMES = {
        "Freestyle project": "Star-Lord-The-Charming-Freestyle",
        "Pipeline": "Gamora_The_Fierce_Pipeline",
        "Multi-configuration project": "Drax_The_Destroyer_MultiConfig",
        "Folder": "Rocket The Clever Folder",
        "Multibranch Pipeline": "Groot_The_Mighty_Multibranch",
        "Organization Folder": "Nebula_The_Ruthless_OrgFolder",
    }

    DEFAULT_PROJECT_DATA_MAP = {
        "Freestyle project": {
            "status": "Not built",
            "weather": "100%",
            "name": PROJECT_NAMES["Freestyle project"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Pipeline": {
            "status": "Not built",
            "weather": "100%",
            "name": PROJECT_NAMES["Pipeline"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Multi-configuration project": {
            "status": "Not built",
            "weather": "100%",
            "name": PROJECT_NAMES["Multi-configuration project"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Folder": {
            "status": "Folder",
            "weather": "100%",
            "name": PROJECT_NAMES["Folder"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Multibranch Pipeline": {
            "status": "Multibranch Pipeline",
            "weather": "100%",
            "name": PROJECT_NAMES["Multibranch Pipeline"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        },
        "Organization Folder": {
            "status": "Organization Folder",
            "weather": "100%",
            "name": PROJECT_NAMES["Organization Folder"],
            "last_success": "N/A",
            "last_failure": "N/A",
            "duration": "N/A",
            "schedule": ""
        }
    }
